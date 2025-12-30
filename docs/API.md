# Go Engine API

This file documents the public API exposed by the Go packages under `go-engine/`.

Package: `pig_caeser`

Files of interest (implementation may be in subpackages):

- `caeser_cypher/caeser_cypher.go`
  - `func CaeserCypher(input string, key int) string`
    - Purpose: Shift letters in `input` forward by `key` positions (A–Z, a–z preserved). Non-letter characters returned unchanged.
    - Inputs: `input` (plaintext string), `key` (shift amount, expected 1..25 in current code).
    - Output: ciphertext string.
  - `func CaeserDecypher(input string, key int) string`
    - Purpose: Reverse the shift by `key`.

- `pig_latin/pig_latin.go`
  - `func PigLatinConv(input string) string`
    - Purpose: Convert `input` to Pig Latin using the project's variant. Current implementation splits on spaces and appends suffixes; see `specs/Pig_latin.md` for rules.
  - `func PigLatinDeconv(input string) string`
    - Purpose: Heuristic reversal of Pig Latin back to base words.

Notes
- The API currently uses string return values and returns human-readable error strings on invalid input. The `specs/errors.md` recommends structured error codes; consider refactoring to `(string, error)` or a typed error with codes to improve programmatic usage.
- For better Unicode support and punctuation preservation, update Pig Latin functions to operate on `[]rune` and implement tokenization that separates leading/trailing punctuation from the alphabetic core.
