package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	if len(os.Args) < 4 || os.Args[1] != "verify" {
		fmt.Println("Usage: mono-verify verify <yaml_file> <ascii_file> [schema_file]")
		os.Exit(1)
	}

	yamlFile := os.Args[2]
	asciiFile := os.Args[3]
	schemaPath := ""
	if len(os.Args) >= 5 {
		schemaPath = os.Args[4]
	} else {
		schemaPath, _ = defaultSchemaPath()
	}

	schemaLabel := schemaPath
	if schemaLabel == "" {
		schemaLabel = "embedded mono-dsl.schema.json"
	}
	fmt.Printf("Validating YAML: %s against schema: %s\n", yamlFile, schemaLabel)
	err := ValidateYAML(schemaPath, yamlFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "YAML validation failed: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Parsing YAML...\n")
	yamlData, err := ParseYAML(yamlFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to parse YAML: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Parsing ASCII: %s\n", asciiFile)
	asciiData, err := ParseASCII(asciiFile, func() string {
		t := ""
		if k, ok := yamlData["kind"].(string); ok {
			t = k
		}
		if k, ok := yamlData["artifact_type"].(string); ok {
			t = k
		}
		return t
	}())
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to parse ASCII: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Verifying YAML elements against ASCII projection...\n")
	err = Verify(yamlData, asciiData)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Verification failed: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Verification successful! All YAML elements correctly projected to ASCII.")
}

func defaultSchemaPath() (string, error) {
	const schemaRel = "dev/designer/mono-dsl.schema.json"

	wd, err := os.Getwd()
	if err == nil {
		if path, ok := findInParents(wd, schemaRel); ok {
			return path, nil
		}
	}

	exe, err := os.Executable()
	if err == nil {
		if path, ok := findInParents(filepath.Dir(exe), schemaRel); ok {
			return path, nil
		}
	}

	return "", fmt.Errorf("%s not found from current directory or executable path", schemaRel)
}

func findInParents(start, rel string) (string, bool) {
	dir, err := filepath.Abs(start)
	if err != nil {
		return "", false
	}
	for {
		candidate := filepath.Join(dir, rel)
		if _, err := os.Stat(candidate); err == nil {
			return candidate, true
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return "", false
		}
		dir = parent
	}
}
