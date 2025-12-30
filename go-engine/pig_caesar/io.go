package pig_caesar

import (
	"errors"
	"os"
)

// ReadInputFile reads the entire input file as bytes.
func ReadInputFile(path string) ([]byte, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, errors.New("failed to read input file")
	}
	return data, nil
}

// WriteOutputFile writes bytes to the output file.
func WriteOutputFile(path string, data []byte) error {
	err := os.WriteFile(path, data, 0644)
	if err != nil {
		return errors.New("failed to write output file")
	}
	return nil
}
