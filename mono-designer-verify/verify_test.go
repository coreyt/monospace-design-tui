package main

import (
	"os"
	"reflect"
	"testing"
)

func TestPreFlightValidation(t *testing.T) {
	// Create a temporary valid YAML
	validYAML := `
id: "test-screen"
title: "Test Screen"
archetype: "admin"
source:
  kind: "generated"
`
	yamlFile := "test_valid.yaml"
	os.WriteFile(yamlFile, []byte(validYAML), 0644)
	defer os.Remove(yamlFile)

	schemaPath := "../dev/designer/mono-dsl.schema.json"

	err := ValidateYAML(schemaPath, yamlFile)
	if err != nil {
		t.Fatalf("Expected valid YAML to pass, got: %v", err)
	}

	invalidYAML := `
id: "test-screen"
title: "Test Screen"
` // missing archetype and source
	invalidFile := "test_invalid.yaml"
	os.WriteFile(invalidFile, []byte(invalidYAML), 0644)
	defer os.Remove(invalidFile)

	err = ValidateYAML(schemaPath, invalidFile)
	if err == nil {
		t.Fatalf("Expected invalid YAML to fail")
	}
}

func TestParseYAML(t *testing.T) {
	yamlContent := `
id: "test"
regions:
  - id: "main"
    role: "content"
`
	yamlFile := "test_parse.yaml"
	os.WriteFile(yamlFile, []byte(yamlContent), 0644)
	defer os.Remove(yamlFile)

	data, err := ParseYAML(yamlFile)
	if err != nil {
		t.Fatalf("Failed to parse YAML: %v", err)
	}

	if data["id"] != "test" {
		t.Errorf("Expected id 'test', got %v", data["id"])
	}
}

func TestParseASCII(t *testing.T) {
	asciiContent := `┌──────────────────────────────────────────────────────────────────────────────┐
│                            Screen Title (screen-id)                          │
├──────────────────────────────────────────────────────────────────────────────┤
│ [MAIN] content area                                                          │
│   • req_list (table): list of requests                                       │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│ ACTIONS: Submit, Cancel                                                      │
├──────────────────────────────────────────────────────────────────────────────┤
│ [enter] Submit [esc] Cancel                                                  │
└──────────────────────────────────────────────────────────────────────────────┘`

	asciiFile := "test_ascii.txt"
	os.WriteFile(asciiFile, []byte(asciiContent), 0644)
	defer os.Remove(asciiFile)

	data, err := ParseASCII(asciiFile)
	if err != nil {
		t.Fatalf("Failed to parse ASCII: %v", err)
	}

	if len(data.Regions) != 1 {
		t.Fatalf("Expected 1 region, got %d", len(data.Regions))
	}
	if data.Regions[0].ID != "MAIN" {
		t.Errorf("Expected region ID 'MAIN', got %s", data.Regions[0].ID)
	}
	if data.Regions[0].Role != "content area" {
		t.Errorf("Expected region Role 'content area', got %s", data.Regions[0].Role)
	}
	if len(data.Regions[0].Components) != 1 {
		t.Fatalf("Expected 1 component, got %d", len(data.Regions[0].Components))
	}
	if data.Regions[0].Components[0].ID != "req_list" {
		t.Errorf("Expected component ID 'req_list', got %s", data.Regions[0].Components[0].ID)
	}
	if data.Regions[0].Components[0].Type != "table" {
		t.Errorf("Expected component Type 'table', got %s", data.Regions[0].Components[0].Type)
	}
	if data.Regions[0].Components[0].Purpose != "list of requests" {
		t.Errorf("Expected component Purpose 'list of requests', got %s", data.Regions[0].Components[0].Purpose)
	}

	expectedActions := []string{"Submit", "Cancel"}
	if !reflect.DeepEqual(data.Actions, expectedActions) {
		t.Errorf("Expected actions %v, got %v", expectedActions, data.Actions)
	}

	if data.FooterKeys["enter"] != "Submit" || data.FooterKeys["esc"] != "Cancel" {
		t.Errorf("Unexpected footer keys: %v", data.FooterKeys)
	}
}

func TestVerifyEngine(t *testing.T) {
	yamlData := map[string]interface{}{
		"regions": []interface{}{
			map[string]interface{}{
				"id":   "main",
				"role": "content area",
			},
		},
		"components": []interface{}{
			map[string]interface{}{
				"id":      "req_list",
				"type":    "table",
				"purpose": "list of requests",
				"region":  "main",
			},
		},
		"actions": []interface{}{
			map[string]interface{}{"label": "Submit"},
			map[string]interface{}{"label": "Cancel"},
		},
		"footer_keys": []interface{}{
			map[string]interface{}{"key": "enter", "label": "Submit"},
			map[string]interface{}{"key": "esc", "label": "Cancel"},
		},
	}

	asciiData := ASCIIData{
		Regions: []RegionData{
			{
				ID:   "MAIN",
				Role: "content area",
				Components: []ComponentData{
					{ID: "req_list", Type: "table", Purpose: "list of requests"},
				},
			},
		},
		Actions: []string{"Submit", "Cancel"},
		FooterKeys: map[string]string{
			"enter": "Submit",
			"esc":   "Cancel",
		},
	}

	err := Verify(yamlData, asciiData)
	if err != nil {
		t.Fatalf("Expected verification to pass, got: %v", err)
	}

	// Make it fail
	yamlData["actions"] = []interface{}{
		map[string]interface{}{"label": "Submit"},
		map[string]interface{}{"label": "MissingAction"},
	}

	err = Verify(yamlData, asciiData)
	if err == nil {
		t.Fatalf("Expected verification to fail due to missing action")
	}
}
