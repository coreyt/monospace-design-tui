package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"os"
	"regexp"
	"strings"

	"github.com/santhosh-tekuri/jsonschema/v5"
	"gopkg.in/yaml.v3"
)

type ASCIIData struct {
	// Screen
	Regions    []RegionData
	Actions    []string
	FooterKeys map[string]string
	ScreenText string
	// Nav
	Workspaces []string
	Routes     []RouteData
	Rules      []string
	// Workflow
	Stages []string
}

type RegionData struct {
	ID         string
	Role       string
	Components []ComponentData
}

type ComponentData struct {
	ID      string
	Type    string
	Purpose string
}

type RouteData struct {
	From    string
	To      string
	Trigger string
}

//go:embed schema/mono-dsl.schema.json
var embeddedSchema string

var nonAlnum = regexp.MustCompile(`[^a-z0-9]+`)

func normalizeText(s string) string {
	s = strings.ToLower(s)
	s = nonAlnum.ReplaceAllString(s, " ")
	return strings.Join(strings.Fields(s), " ")
}

func containsNormalized(haystack, needle string) bool {
	needle = normalizeText(needle)
	if needle == "" {
		return true
	}
	return strings.Contains(normalizeText(haystack), needle)
}

func containsAllWords(haystack, needle string) bool {
	haystackWords := map[string]bool{}
	for _, word := range strings.Fields(normalizeText(haystack)) {
		haystackWords[word] = true
	}
	for _, word := range strings.Fields(normalizeText(needle)) {
		if !haystackWords[word] {
			return false
		}
	}
	return strings.TrimSpace(needle) != ""
}

func parseFooterKeys(line string, footerKeys map[string]string) {
	fields := strings.Fields(line)
	for i := 0; i+1 < len(fields); i += 2 {
		key := strings.Trim(fields[i], "[]")
		label := strings.Trim(fields[i+1], "[]")
		if key != "" && label != "" {
			footerKeys[key] = label
		}
	}
}

func artifactType(yamlData map[string]interface{}) string {
	if k, ok := yamlData["kind"].(string); ok {
		return k
	}
	if k, ok := yamlData["artifact_type"].(string); ok {
		return k
	}
	return ""
}

func componentVisible(compMap map[string]interface{}, asciiData ASCIIData) bool {
	id, _ := compMap["id"].(string)
	typ, _ := compMap["type"].(string)
	purpose, _ := compMap["purpose"].(string)
	regionID, _ := compMap["region"].(string)
	for _, asciiReg := range asciiData.Regions {
		if !strings.EqualFold(asciiReg.ID, regionID) {
			continue
		}
		for _, asciiComp := range asciiReg.Components {
			if strings.EqualFold(asciiComp.ID, id) {
				if typ != "" && !strings.EqualFold(asciiComp.Type, typ) {
					return false
				}
				return purpose == "" || strings.EqualFold(asciiComp.Purpose, purpose)
			}
		}
	}
	if containsNormalized(asciiData.ScreenText, id) {
		return true
	}
	if containsNormalized(asciiData.ScreenText, strings.ReplaceAll(id, "-", " ")) {
		return true
	}
	if containsAllWords(asciiData.ScreenText, strings.ReplaceAll(id, "-", " ")) {
		return true
	}
	return containsNormalized(asciiData.ScreenText, purpose) || containsAllWords(asciiData.ScreenText, purpose)
}

func verifyFooterKeys(rawKeys []interface{}, asciiData ASCIIData) error {
	for _, rawKey := range rawKeys {
		keyMap, ok := rawKey.(map[string]interface{})
		if !ok {
			continue
		}
		key, _ := keyMap["key"].(string)
		label, _ := keyMap["label"].(string)
		if asciiLabel, exists := asciiData.FooterKeys[key]; exists {
			if strings.EqualFold(asciiLabel, label) {
				continue
			}
			return fmt.Errorf("footer key '%s' label mismatch: expected %s, got %s", key, label, asciiLabel)
		}
		if !containsNormalized(asciiData.ScreenText, key) {
			return fmt.Errorf("footer key '%s' defined in YAML not found in ASCII", key)
		}
		labelWords := strings.Fields(label)
		if label != "" && !containsNormalized(asciiData.ScreenText, label) && (len(labelWords) == 0 || !containsNormalized(asciiData.ScreenText, labelWords[0])) {
			return fmt.Errorf("footer key '%s' label mismatch: expected %s", key, label)
		}
	}
	return nil
}

func ValidateYAML(schemaPath, yamlPath string) error {
	schemaCompiler := jsonschema.NewCompiler()
	schemaLocation := schemaPath
	if schemaLocation == "" {
		schemaLocation = "mono-dsl.schema.json"
		if err := schemaCompiler.AddResource(schemaLocation, strings.NewReader(embeddedSchema)); err != nil {
			return err
		}
	}
	sch, err := schemaCompiler.Compile(schemaLocation)
	if err != nil {
		return err
	}
	yamlData, err := os.ReadFile(yamlPath)
	if err != nil {
		return err
	}
	var rawObj interface{}
	err = yaml.Unmarshal(yamlData, &rawObj)
	if err != nil {
		return err
	}
	rawObj = fixMaps(rawObj)
	err = sch.Validate(rawObj)
	if err != nil {
		return fmt.Errorf("schema validation failed: %w", err)
	}
	return nil
}

func fixMaps(v interface{}) interface{} {
	switch v := v.(type) {
	case []interface{}:
		for i, val := range v {
			v[i] = fixMaps(val)
		}
	case map[interface{}]interface{}:
		newMap := make(map[string]interface{})
		for k, val := range v {
			newMap[fmt.Sprintf("%v", k)] = fixMaps(val)
		}
		return newMap
	case map[string]interface{}:
		for k, val := range v {
			v[k] = fixMaps(val)
		}
	}
	return v
}

func ParseYAML(yamlPath string) (map[string]interface{}, error) {
	yamlData, err := os.ReadFile(yamlPath)
	if err != nil {
		return nil, err
	}
	var result map[string]interface{}
	err = yaml.Unmarshal(yamlData, &result)
	if err != nil {
		return nil, err
	}
	return result, nil
}

func ParseASCII(asciiPath string, artifactType string) (ASCIIData, error) {
	file, err := os.Open(asciiPath)
	if err != nil {
		return ASCIIData{}, err
	}
	defer file.Close()

	var data ASCIIData
	data.FooterKeys = make(map[string]string)
	scanner := bufio.NewScanner(file)

	if artifactType == "screen" {
		var currentRegion *RegionData
		dividerCount := 0
		var screenLines []string
		for scanner.Scan() {
			line := scanner.Text()
			if strings.HasPrefix(line, "├") {
				dividerCount++
				continue
			}
			if strings.HasPrefix(line, "┌") || strings.HasPrefix(line, "└") {
				continue
			}
			line = strings.Trim(line, "│ \t\r\n")
			if line == "" {
				continue
			}
			screenLines = append(screenLines, line)

			if dividerCount == 1 {
				if strings.HasPrefix(line, "[") {
					parts := strings.SplitN(line, "]", 2)
					if len(parts) == 2 {
						id := strings.TrimPrefix(parts[0], "[")
						if currentRegion != nil {
							data.Regions = append(data.Regions, *currentRegion)
						}
						currentRegion = &RegionData{ID: id, Role: strings.TrimSpace(parts[1])}
					}
				} else if strings.HasPrefix(line, "•") {
					line = strings.TrimSpace(strings.TrimPrefix(line, "•"))
					parts := strings.SplitN(line, ":", 2)
					if len(parts) == 2 {
						left := strings.TrimSpace(parts[0])
						idType := strings.SplitN(left, " (", 2)
						id := strings.TrimSpace(idType[0])
						typ := ""
						if len(idType) == 2 {
							typ = strings.TrimSuffix(idType[1], ")")
						}
						if currentRegion != nil {
							currentRegion.Components = append(currentRegion.Components, ComponentData{
								ID: id, Type: typ, Purpose: strings.TrimSpace(parts[1]),
							})
						}
					}
				}
			} else if dividerCount >= 2 {
				if strings.HasPrefix(line, "ACTIONS:") {
					actions := strings.Split(strings.TrimPrefix(line, "ACTIONS:"), ",")
					for _, a := range actions {
						if lbl := strings.TrimSpace(a); lbl != "" {
							data.Actions = append(data.Actions, lbl)
						}
					}
				}
				parseFooterKeys(line, data.FooterKeys)
			}
		}
		if currentRegion != nil {
			data.Regions = append(data.Regions, *currentRegion)
		}
		data.ScreenText = strings.Join(screenLines, "\n")
	} else if artifactType == "navigation" {
		dividerCount := 0
		for scanner.Scan() {
			line := scanner.Text()
			if strings.HasPrefix(line, "├") {
				dividerCount++
				continue
			}
			if strings.HasPrefix(line, "┌") || strings.HasPrefix(line, "└") {
				continue
			}
			line = strings.Trim(line, "│ \t\r\n")
			if line == "" {
				continue
			}

			if dividerCount == 0 {
				if strings.HasPrefix(line, "[") {
					data.Workspaces = append(data.Workspaces, strings.TrimSuffix(strings.TrimPrefix(line, "["), "]"))
				}
			} else if dividerCount == 1 {
				parts := strings.Split(line, "->")
				if len(parts) == 3 {
					data.Routes = append(data.Routes, RouteData{
						From:    strings.TrimSpace(parts[0]),
						Trigger: strings.TrimSpace(parts[1]),
						To:      strings.TrimSpace(parts[2]),
					})
				}
			} else if dividerCount == 2 {
				rules := strings.Split(line, "|")
				for _, r := range rules {
					data.Rules = append(data.Rules, strings.TrimSpace(r))
				}
			}
		}
	} else if artifactType == "workflow" {
		for scanner.Scan() {
			line := strings.TrimSpace(scanner.Text())
			if strings.HasPrefix(line, "-") {
				data.Stages = append(data.Stages, strings.TrimSpace(strings.TrimPrefix(line, "-")))
			}
		}
	}

	return data, scanner.Err()
}

func Verify(yamlData map[string]interface{}, asciiData ASCIIData) error {
	aType := artifactType(yamlData)

	if aType == "screen" {
		visibleComponentsByRegion := map[string]bool{}
		footerRegions := map[string]bool{}

		if rawRegions, ok := yamlData["regions"].([]interface{}); ok {
			for _, rawReg := range rawRegions {
				regMap, ok := rawReg.(map[string]interface{})
				if !ok {
					continue
				}
				id, _ := regMap["id"].(string)
				typ, _ := regMap["type"].(string)
				if typ == "footer" {
					footerRegions[id] = true
				}
			}
		}

		if rawComps, ok := yamlData["components"].([]interface{}); ok {
			for _, rawComp := range rawComps {
				compMap, ok := rawComp.(map[string]interface{})
				if !ok {
					continue
				}
				id, _ := compMap["id"].(string)
				regionID, _ := compMap["region"].(string)
				if footerRegions[regionID] {
					continue
				}
				if !componentVisible(compMap, asciiData) {
					return fmt.Errorf("component %s defined in YAML not found in ASCII", id)
				}
				visibleComponentsByRegion[regionID] = true
			}
		}

		if rawRegions, ok := yamlData["regions"].([]interface{}); ok {
			for _, rawReg := range rawRegions {
				regMap, ok := rawReg.(map[string]interface{})
				if !ok {
					continue
				}
				id, _ := regMap["id"].(string)
				role, _ := regMap["role"].(string)
				typ, _ := regMap["type"].(string)
				if typ == "footer" {
					continue
				}
				if !visibleComponentsByRegion[id] && !containsNormalized(asciiData.ScreenText, role) {
					return fmt.Errorf("region %s defined in YAML not represented in ASCII", id)
				}
			}
		}

		if rawKeys, ok := yamlData["footer_keys"].([]interface{}); ok {
			if err := verifyFooterKeys(rawKeys, asciiData); err != nil {
				return err
			}
		} else if rawKeyMap, ok := yamlData["footer_keys"].(map[string]interface{}); ok {
			if bindings, ok := rawKeyMap["bindings"].([]interface{}); ok {
				if err := verifyFooterKeys(bindings, asciiData); err != nil {
					return err
				}
			}
		}
	} else if aType == "navigation" {
		if rawWorkspaces, ok := yamlData["workspaces"].([]interface{}); ok {
			for _, rawWs := range rawWorkspaces {
				wsMap, ok := rawWs.(map[string]interface{})
				if !ok {
					continue
				}
				label, _ := wsMap["label"].(string)
				found := false
				for _, asciiWs := range asciiData.Workspaces {
					if strings.EqualFold(asciiWs, label) {
						found = true
						break
					}
				}
				if !found {
					return fmt.Errorf("workspace '%s' defined in YAML not found in ASCII", label)
				}
			}
		}
		if rawRoutes, ok := yamlData["routes"].([]interface{}); ok {
			for _, rawR := range rawRoutes {
				rMap, ok := rawR.(map[string]interface{})
				if !ok {
					continue
				}
				from, _ := rMap["from"].(string)
				to, _ := rMap["to"].(string)
				trigger, _ := rMap["trigger"].(string)
				found := false
				for _, asciiR := range asciiData.Routes {
					if containsNormalized(asciiR.From, from) && containsNormalized(asciiR.Trigger, trigger) && containsNormalized(asciiR.To, to) {
						found = true
						break
					}
				}
				if !found && trigger != "" {
					return fmt.Errorf("route '%s -> %s' defined in YAML not found in ASCII", from, trigger)
				}
			}
		}
	} else if aType == "workflow" {
		if rawStages, ok := yamlData["stages"].([]interface{}); ok {
			for _, rawS := range rawStages {
				sMap, ok := rawS.(map[string]interface{})
				if !ok {
					continue
				}
				label, _ := sMap["label"].(string)
				found := false
				for _, asciiS := range asciiData.Stages {
					if strings.EqualFold(asciiS, label) {
						found = true
						break
					}
				}
				if !found {
					return fmt.Errorf("stage '%s' defined in YAML not found in ASCII", label)
				}
			}
		}
	}
	return nil
}
