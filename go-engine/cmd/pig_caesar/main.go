package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/fco1000/piglatin_caeser_encryption/go-engine/pig_caesar"
)

func main() {
	// CLI flags
	mode := flag.String("mode", "encrypt", "encrypt or decrypt")
	inputPath := flag.String("input", "", "input file path")
	outputPath := flag.String("output", "", "output file path")
	key := flag.Int("key", 0, "caesar cipher key (1..25)")

	flag.Parse()

	// basic validation
	if *inputPath == "" || *outputPath == "" {
		fmt.Fprintln(os.Stderr, "input and output paths are required")
		os.Exit(1)
	}

	if *key < 1 || *key > 25 {
		fmt.Fprintln(os.Stderr, "enter valid key value above 1 but below 25")
		os.Exit(1)
	}

	// read input file
	data, err := os.ReadFile(*inputPath)
	if err != nil {
		fmt.Fprintln(os.Stderr, "failed to read input file:", err)
		os.Exit(1)
	}

	text := string(data)
	var result string

	// pipeline
	switch *mode {
	case "encrypt":
		pl := pig_caesar.PigLatinConv(text)
		result = pig_caesar.CaeserCypher(pl, *key)

	case "decrypt":
		cd := pig_caesar.CaeserDecypher(text, *key)
		result = pig_caesar.PigLatinDeconv(cd)

	default:
		fmt.Fprintln(os.Stderr, "invalid mode:", *mode)
		os.Exit(1)
	}

	// write output file
	err = os.WriteFile(*outputPath, []byte(result), 0644)
	if err != nil {
		fmt.Fprintln(os.Stderr, "failed to write output file:", err)
		os.Exit(1)
	}

	// also print to stdout for Python CLI capture
	fmt.Print(result)
}
