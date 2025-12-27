# Error codes — pig latin & caesar cipher tool

All error codes are shared and must match exactly between implementations (Python & Go). Use the codes below for programmatic checks; human-friendly messages may be derived from the code.

| Code | Name | Applies to | Meaning |
|------|------|------------|---------|
| 0 | OK | Both | Success |
| 1 | ERR_EMPTY_INPUT | Both | Input string is empty |
| 2 | ERR_NO_WORDS | Pig Latin | No words found to transform |
| 3 | ERR_NON_ALPHA_WORD | Pig Latin | Word contains non-alphabetic characters where letters are required |
| 4 | ERR_TOO_LONG_INPUT | Both | Input exceeds allowed length |
| 5 | ERR_INVALID_SHIFT | Caesar | Shift/key is missing or not an integer |
| 6 | ERR_SHIFT_OUT_OF_RANGE | Caesar | Shift is outside allowed range (e.g., <0 or >25) |
| 7 | ERR_IO | Both | I/O error (reading/writing files or streams) |
| 8 | ERR_INTERNAL | Both | Internal error / unexpected condition |

Suggested short messages (for logs or user output) should be deterministic from the code (e.g., map code -> message).

Python reference (errors.py)
```python
# errors.py - shared error codes and exception
OK = 0
ERR_EMPTY_INPUT = 1
ERR_NO_WORDS = 2
ERR_NON_ALPHA_WORD = 3
ERR_TOO_LONG_INPUT = 4
ERR_INVALID_SHIFT = 5
ERR_SHIFT_OUT_OF_RANGE = 6
ERR_IO = 7
ERR_INTERNAL = 8

class PigCipherError(Exception):
    def __init__(self, code, message=None):
        self.code = code
        self.message = message or ERROR_MESSAGES.get(code, "Unknown error")
        super().__init__(self.message)

# optional map for user messages
ERROR_MESSAGES = {
    OK: "Success",
    ERR_EMPTY_INPUT: "Input is empty",
    ERR_NO_WORDS: "No words found",
    ERR_NON_ALPHA_WORD: "Word contains non-alpha characters",
    ERR_TOO_LONG_INPUT: "Input too long",
    ERR_INVALID_SHIFT: "Invalid shift (not an integer)",
    ERR_SHIFT_OUT_OF_RANGE: "Shift out of range",
    ERR_IO: "I/O error",
    ERR_INTERNAL: "Internal error",
}
```

Go reference (errors.go)
```go
// errors.go - shared error codes and typed error
package errors

type Code int

const (
    OK Code = iota
    ERR_EMPTY_INPUT
    ERR_NO_WORDS
    ERR_NON_ALPHA_WORD
    ERR_TOO_LONG_INPUT
    ERR_INVALID_SHIFT
    ERR_SHIFT_OUT_OF_RANGE
    ERR_IO
    ERR_INTERNAL
)

var ErrorMessages = map[Code]string{
    OK:                    "Success",
    ERR_EMPTY_INPUT:       "Input is empty",
    ERR_NO_WORDS:          "No words found",
    ERR_NON_ALPHA_WORD:    "Word contains non-alpha characters",
    ERR_TOO_LONG_INPUT:    "Input too long",
    ERR_INVALID_SHIFT:     "Invalid shift (not an integer)",
    ERR_SHIFT_OUT_OF_RANGE:"Shift out of range",
    ERR_IO:                "I/O error",
    ERR_INTERNAL:          "Internal error",
}

type PigCipherError struct {
    Code Code
    Msg  string
}

func (e PigCipherError) Error() string {
    if e.Msg != "" {
        return e.Msg
    }
    return ErrorMessages[e.Code]
}

func New(code Code, msg string) error {
    return PigCipherError{Code: code, Msg: msg}
}
```

Usage patterns
- Python: raise PigCipherError(ERR_INVALID_SHIFT) or raise PigCipherError(ERR_NON_ALPHA_WORD, "word: '123'")
- Go: return nil, errors.New(errors.ERR_INVALID_SHIFT, "") or return "", errors.PigCipherError{Code: errors.ERR_NON_ALPHA_WORD, Msg: "word: '123'"}

Notes
- Keep integer values and constant names identical between files.
- Map codes to localized/extended messages only at the UI/log layer; use codes for control flow and tests.
- Adjust range rules (e.g., allowed shift range) in project docs but keep code constants stable.