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
        // Screen
        Regions    []RegionData
        Actions    []string
        FooterKeys map[string]string
        // Nav
        Workspaces []string
        Routes     []RouteData
        Rules      []string
        // Workflow
        Stages     []string
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
                for scanner.Scan() {
                        line := scanner.Text()
                        if strings.HasPrefix(line, "├") {
                                dividerCount++
                                continue
                        }
                        if strings.HasPrefix(line, "┌") || strings.HasPrefix(line, "└") { continue }
                        line = strings.Trim(line, "│ \t\r\n")
                        if line == "" { continue }

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
                                                if len(idType) == 2 { typ = strings.TrimSuffix(idType[1], ")") }
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
                                                if lbl := strings.TrimSpace(a); lbl != "" { data.Actions = append(data.Actions, lbl) }
                                        }
                                } else if strings.HasPrefix(line, "[") {
                                        parts := strings.Split(line, "[")
                                        for _, part := range parts {
                                                if part == "" { continue }
                                                subparts := strings.SplitN(part, "]", 2)
                                                if len(subparts) == 2 {
                                                        if key, label := strings.TrimSpace(subparts[0]), strings.TrimSpace(subparts[1]); key != "" && label != "" {
                                                                data.FooterKeys[key] = label
                                                        }
                                                }
                                        }
                                }
                        }
                }
                if currentRegion != nil { data.Regions = append(data.Regions, *currentRegion) }
        } else if artifactType == "navigation" {
                dividerCount := 0
                for scanner.Scan() {
                        line := scanner.Text()
                        if strings.HasPrefix(line, "├") {
                                dividerCount++
                                continue
                        }
                        if strings.HasPrefix(line, "┌") || strings.HasPrefix(line, "└") { continue }
                        line = strings.Trim(line, "│ \t\r\n")
                        if line == "" { continue }

                        if dividerCount == 0 {
                                if strings.HasPrefix(line, "[") {
                                        data.Workspaces = append(data.Workspaces, strings.TrimSuffix(strings.TrimPrefix(line, "["), "]"))
                                }
                        } else if dividerCount == 1 {
                                parts := strings.Split(line, "->")
                                if len(parts) == 3 {
                                        data.Routes = append(data.Routes, RouteData{
                                                From: strings.TrimSpace(parts[0]),
                                                Trigger: strings.TrimSpace(parts[1]),
                                                To: strings.TrimSpace(parts[2]),
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
        aType := ""
        if k, ok := yamlData["kind"].(string); ok { aType = k }
        if k, ok := yamlData["artifact_type"].(string); ok { aType = k }

        if aType == "screen" {
                if rawRegions, ok := yamlData["regions"].([]interface{}); ok {
                        for _, rawReg := range rawRegions {
                                regMap, ok := rawReg.(map[string]interface{})
                                if !ok { continue }
                                id, _ := regMap["id"].(string)
                                role, _ := regMap["role"].(string)
                                found := false
                                for _, asciiReg := range asciiData.Regions {
                                        if strings.EqualFold(asciiReg.ID, id) {
                                                found = true
                                                if !strings.EqualFold(asciiReg.Role, role) { return fmt.Errorf("region %s role mismatch: expected %s, got %s", id, role, asciiReg.Role) }
                                                break
                                        }
                                }
                                typ, _ := regMap["type"].(string)
                                if !found && typ != "footer" { return fmt.Errorf("region %s defined in YAML not found in ASCII", id) }
                        }
                }
                if rawComps, ok := yamlData["components"].([]interface{}); ok {
                        for _, rawComp := range rawComps {
                                compMap, ok := rawComp.(map[string]interface{})
                                if !ok { continue }
                                id, _ := compMap["id"].(string)
                                typ, _ := compMap["type"].(string)
                                purpose, _ := compMap["purpose"].(string)
                                regionId, _ := compMap["region"].(string)
                                found := false
                                for _, asciiReg := range asciiData.Regions {
                                        if strings.EqualFold(asciiReg.ID, regionId) {
                                                for _, asciiComp := range asciiReg.Components {
                                                        if strings.EqualFold(asciiComp.ID, id) {
                                                                found = true
                                                                if !strings.EqualFold(asciiComp.Type, typ) { return fmt.Errorf("component %s type mismatch", id) }
                                                                if !strings.EqualFold(asciiComp.Purpose, purpose) { return fmt.Errorf("component %s purpose mismatch", id) }
                                                                break
                                                        }
                                                }
                                        }
                                }
                                isFooterComp := false
                                if rawRegions, ok := yamlData["regions"].([]interface{}); ok {
                                        for _, rawReg := range rawRegions {
                                                regMap, _ := rawReg.(map[string]interface{})
                                                if regMap["id"] == regionId && regMap["type"] == "footer" { isFooterComp = true }
                                        }
                                }
                                if !found && !isFooterComp { return fmt.Errorf("component %s (region %s) defined in YAML not found in ASCII", id, regionId) }
                        }
                }
                if rawActions, ok := yamlData["actions"].([]interface{}); ok {
                        for _, rawAct := range rawActions {
                                actMap, ok := rawAct.(map[string]interface{})
                                if !ok { continue }
                                label, _ := actMap["label"].(string)
                                found := false
                                for _, asciiAct := range asciiData.Actions {
                                        if strings.EqualFold(asciiAct, label) { found = true; break }
                                }
                                if !found { return fmt.Errorf("action label '%s' defined in YAML not found in ASCII", label) }
                        }
                }
                if rawKeys, ok := yamlData["footer_keys"].([]interface{}); ok {
                        for _, rawKey := range rawKeys {
                                keyMap, ok := rawKey.(map[string]interface{})
                                if !ok { continue }
                                key, _ := keyMap["key"].(string)
                                label, _ := keyMap["label"].(string)
                                asciiLabel, exists := asciiData.FooterKeys[key]
                                if !exists { return fmt.Errorf("footer key '%s' defined in YAML not found in ASCII", key) }
                                if !strings.EqualFold(asciiLabel, label) { return fmt.Errorf("footer key '%s' label mismatch: expected %s, got %s", key, label, asciiLabel) }
                        }
                }
        } else if aType == "navigation" {
                if rawWorkspaces, ok := yamlData["workspaces"].([]interface{}); ok {
                        for _, rawWs := range rawWorkspaces {
                                wsMap, ok := rawWs.(map[string]interface{})
                                if !ok { continue }
                                label, _ := wsMap["label"].(string)
                                found := false
                                for _, asciiWs := range asciiData.Workspaces {
                                        if strings.EqualFold(asciiWs, label) { found = true; break }
                                }
                                if !found { return fmt.Errorf("workspace '%s' defined in YAML not found in ASCII", label) }
                        }
                }
                if rawRoutes, ok := yamlData["routes"].([]interface{}); ok {
                        for _, rawR := range rawRoutes {
                                rMap, ok := rawR.(map[string]interface{})
                                if !ok { continue }
                                from, _ := rMap["from"].(string)
                                trigger, _ := rMap["trigger"].(string)
                                found := false
                                for _, asciiR := range asciiData.Routes {
                                        if strings.EqualFold(asciiR.From, from) && strings.EqualFold(asciiR.Trigger, trigger) { found = true; break }
                                }
                                if !found && trigger != "" { return fmt.Errorf("route '%s -> %s' defined in YAML not found in ASCII", from, trigger) }
                        }
                }
        } else if aType == "workflow" {
                if rawStages, ok := yamlData["stages"].([]interface{}); ok {
                        for _, rawS := range rawStages {
                                sMap, ok := rawS.(map[string]interface{})
                                if !ok { continue }
                                label, _ := sMap["label"].(string)
                                found := false
                                for _, asciiS := range asciiData.Stages {
                                        if strings.EqualFold(asciiS, label) { found = true; break }
                                }
                                if !found { return fmt.Errorf("stage '%s' defined in YAML not found in ASCII", label) }
                        }
                }
        }
        return nil
}
