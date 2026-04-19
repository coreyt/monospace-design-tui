package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 4 || os.Args[1] != "verify" {
		fmt.Println("Usage: mono-verify verify <yaml_file> <ascii_file>")
		os.Exit(1)
	}

	yamlFile := os.Args[2]
	asciiFile := os.Args[3]
	schemaPath := "../dev/designer/mono-dsl.schema.json"

	fmt.Printf("Validating YAML: %s against schema: %s\n", yamlFile, schemaPath)
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
                if k, ok := yamlData["kind"].(string); ok { t = k }
                if k, ok := yamlData["artifact_type"].(string); ok { t = k }
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
