package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/santhosh-tekuri/jsonschema/v5"
	"gopkg.in/yaml.v3"
)

type ASCIIData struct {
	Regions    []RegionData
	Actions    []string
	FooterKeys map[string]string
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

func ValidateYAML(schemaPath, yamlPath string) error {
	schemaCompiler := jsonschema.NewCompiler()
	sch, err := schemaCompiler.Compile(schemaPath)
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

func ParseASCII(asciiPath string) (ASCIIData, error) {
	file, err := os.Open(asciiPath)
	if err != nil {
		return ASCIIData{}, err
	}
	defer file.Close()

	var data ASCIIData
	data.FooterKeys = make(map[string]string)
	var currentRegion *RegionData

	scanner := bufio.NewScanner(file)
	
	// dividerCount tracks structural sections
	// 0 = Header
	// 1 = Body (Regions/Components)
	// 2+ = Actions or Footer
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

		if dividerCount == 1 {
			// Body section: Regions and Components
			if strings.HasPrefix(line, "[") {
				parts := strings.SplitN(line, "]", 2)
				if len(parts) == 2 {
					id := strings.TrimPrefix(parts[0], "[")
					role := strings.TrimSpace(parts[1])
					
					if currentRegion != nil {
						data.Regions = append(data.Regions, *currentRegion)
					}
					currentRegion = &RegionData{
						ID:   id,
						Role: role,
					}
				}
			} else if strings.HasPrefix(line, "•") {
				line = strings.TrimPrefix(line, "•")
				line = strings.TrimSpace(line)
				
				parts := strings.SplitN(line, ":", 2)
				if len(parts) == 2 {
					left := strings.TrimSpace(parts[0])
					purpose := strings.TrimSpace(parts[1])
					
					idType := strings.SplitN(left, " (", 2)
					id := strings.TrimSpace(idType[0])
					typ := ""
					if len(idType) == 2 {
						typ = strings.TrimSuffix(idType[1], ")")
					}
					
					if currentRegion != nil {
						currentRegion.Components = append(currentRegion.Components, ComponentData{
							ID:      id,
							Type:    typ,
							Purpose: purpose,
						})
					}
				}
			}
		} else if dividerCount >= 2 {
			// Actions or Footer Key Strip
			if strings.HasPrefix(line, "ACTIONS:") {
				line = strings.TrimPrefix(line, "ACTIONS:")
				actions := strings.Split(line, ",")
				for _, a := range actions {
					label := strings.TrimSpace(a)
					if label != "" {
						data.Actions = append(data.Actions, label)
					}
				}
			} else if strings.HasPrefix(line, "[") {
				// Footer keys format: [enter] Submit [esc] Cancel
				parts := strings.Split(line, "[")
				for _, part := range parts {
					if part == "" {
						continue
					}
					subparts := strings.SplitN(part, "]", 2)
					if len(subparts) == 2 {
						key := strings.TrimSpace(subparts[0])
						label := strings.TrimSpace(subparts[1])
						
						// If there are multiple footer keys, the label might contain spaces before the next '['.
						// The split above actually splits by '[', so 'part' is "enter] Submit "
						// subparts[1] is "Submit ". TrimSpace handles this correctly!
						if key != "" && label != "" {
							data.FooterKeys[key] = label
						}
					}
				}
			}
		}
	}
	
	if currentRegion != nil {
		data.Regions = append(data.Regions, *currentRegion)
	}

	return data, scanner.Err()
}

func Verify(yamlData map[string]interface{}, asciiData ASCIIData) error {
	// Verify Regions
	if rawRegions, ok := yamlData["regions"].([]interface{}); ok {
		for _, rawReg := range rawRegions {
			regMap, ok := rawReg.(map[string]interface{})
			if !ok {
				continue
			}
			
			id, _ := regMap["id"].(string)
			role, _ := regMap["role"].(string)
			
			// find region in asciiData
			found := false
			for _, asciiReg := range asciiData.Regions {
				if strings.EqualFold(asciiReg.ID, id) {
					found = true
					if !strings.EqualFold(asciiReg.Role, role) {
						return fmt.Errorf("region %s role mismatch: expected %s, got %s", id, role, asciiReg.Role)
					}
					break
				}
			}
			// In python code: if region.type == "footer": continue
			// Therefore, if yaml region type is "footer", it might not be in ascii output as a regular region.
			typ, _ := regMap["type"].(string)
			if !found && typ != "footer" {
				return fmt.Errorf("region %s defined in YAML not found in ASCII", id)
			}
		}
	}

	// Verify Components
	if rawComps, ok := yamlData["components"].([]interface{}); ok {
		for _, rawComp := range rawComps {
			compMap, ok := rawComp.(map[string]interface{})
			if !ok {
				continue
			}
			
			id, _ := compMap["id"].(string)
			typ, _ := compMap["type"].(string)
			purpose, _ := compMap["purpose"].(string)
			regionId, _ := compMap["region"].(string)
			
			// Find component in asciiData
			found := false
			for _, asciiReg := range asciiData.Regions {
				if strings.EqualFold(asciiReg.ID, regionId) {
					for _, asciiComp := range asciiReg.Components {
						if strings.EqualFold(asciiComp.ID, id) {
							found = true
							if !strings.EqualFold(asciiComp.Type, typ) {
								return fmt.Errorf("component %s type mismatch: expected %s, got %s", id, typ, asciiComp.Type)
							}
							if !strings.EqualFold(asciiComp.Purpose, purpose) {
								return fmt.Errorf("component %s purpose mismatch: expected %s, got %s", id, purpose, asciiComp.Purpose)
							}
							break
						}
					}
				}
			}
			
			// Only verify components not in the footer region
			isFooterComp := false
			if rawRegions, ok := yamlData["regions"].([]interface{}); ok {
				for _, rawReg := range rawRegions {
					regMap, _ := rawReg.(map[string]interface{})
					if regMap["id"] == regionId && regMap["type"] == "footer" {
						isFooterComp = true
					}
				}
			}

			if !found && !isFooterComp {
				return fmt.Errorf("component %s (region %s) defined in YAML not found in ASCII", id, regionId)
			}
		}
	}

	// Verify Actions
	if rawActions, ok := yamlData["actions"].([]interface{}); ok {
		for _, rawAct := range rawActions {
			actMap, ok := rawAct.(map[string]interface{})
			if !ok {
				continue
			}
			
			label, _ := actMap["label"].(string)
			
			found := false
			for _, asciiAct := range asciiData.Actions {
				if strings.EqualFold(asciiAct, label) {
					found = true
					break
				}
			}
			if !found {
				return fmt.Errorf("action label '%s' defined in YAML not found in ASCII", label)
			}
		}
	}

	// Verify Footer Keys
	if rawKeys, ok := yamlData["footer_keys"].([]interface{}); ok {
		for _, rawKey := range rawKeys {
			keyMap, ok := rawKey.(map[string]interface{})
			if !ok {
				continue
			}
			
			key, _ := keyMap["key"].(string)
			label, _ := keyMap["label"].(string)
			
			asciiLabel, exists := asciiData.FooterKeys[key]
			if !exists {
				return fmt.Errorf("footer key '%s' defined in YAML not found in ASCII", key)
			}
			if !strings.EqualFold(asciiLabel, label) {
				return fmt.Errorf("footer key '%s' label mismatch: expected %s, got %s", key, label, asciiLabel)
			}
		}
	}

	return nil
}
