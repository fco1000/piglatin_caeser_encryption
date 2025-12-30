package pig_caesar

import (
	"errors"
	"fmt"
)

var (
	ErrShiftZero        = errors.New("shift must not be zero")
	ErrShiftOutOfRange  = errors.New("shift out of allowed range (-25..25)")
)

// ValidateShift checks if a shift value is acceptable for a Caesar cipher.
func ValidateShift(shift int) error {
	if shift == 0 {
		return ErrShiftZero
	}
	if shift < -25 || shift > 25 {
		return fmt.Errorf("%w: %d", ErrShiftOutOfRange, shift)
	}
	return nil
}