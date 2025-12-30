package pig_caesar

import (
	"errors"
)

// Encrypt runs the forward transformation pipeline.
func Encrypt(data []byte, cfg *Config) ([]byte, error) {
	if cfg.CaesarShift == 0 {
		return nil, errors.New("invalid Caesar shift")
	}

	text := string(data)

	if cfg.PigLatinOn {
		text = PigLatinConv(text)
	}

	text = CaeserCypher(text, cfg.CaesarShift)

	return []byte(text), nil
}

// Decrypt runs the reverse transformation pipeline.
func Decrypt(data []byte, cfg *Config) ([]byte, error) {
	if cfg.CaesarShift == 0 {
		return nil, errors.New("invalid Caesar shift")
	}

	text := string(data)

	text = CaeserDecypher(text, cfg.CaesarShift)

	if cfg.PigLatinOn {
		text = PigLatinDeconv(text)
	}

	return []byte(text), nil
}
