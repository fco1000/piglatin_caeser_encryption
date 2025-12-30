package pig_caesar

import (
	"errors"
	"os"
	"strings"
)

// Mode defines what the engine should do.
type Mode string

const (
	ModeEncrypt Mode = "encrypt"
	ModeDecrypt Mode = "decrypt"
)

// Config represents the full intent of a single run.
type Config struct {
	Mode        Mode
	InputPath   string
	OutputPath  string
	Password    string
	CaesarShift int
	PigLatinOn  bool
}

// NewConfigFromArgs builds a Config from raw arguments passed by Python.
func NewConfigFromArgs(mode, input, output, password string, pigLatinOn bool) (*Config, error) {
	cfg := &Config{
		Mode:       Mode(strings.ToLower(mode)),
		InputPath:  input,
		OutputPath: output,
		Password:   password,
		PigLatinOn: pigLatinOn,
	}

	if err := cfg.validate(); err != nil {
		return nil, err
	}

	cfg.CaesarShift = deriveShiftFromPassword(cfg.Password)
	return cfg, nil
}

// validate checks if the config makes sense.
func (c *Config) validate() error {
	if c.Mode != ModeEncrypt && c.Mode != ModeDecrypt {
		return errors.New("invalid mode, must be encrypt or decrypt")
	}

	if c.InputPath == "" {
		return errors.New("input path is required")
	}

	if c.OutputPath == "" {
		return errors.New("output path is required")
	}

	if _, err := os.Stat(c.InputPath); err != nil {
		return errors.New("input file does not exist or cannot be accessed")
	}

	if c.Password == "" {
		return errors.New("password must not be empty")
	}

	return nil
}

// deriveShiftFromPassword converts password length into a Caesar shift.
func deriveShiftFromPassword(password string) int {
	shift := len(password) % 26
	if shift == 0 {
		shift = 1
	}
	return shift
}
