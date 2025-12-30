# Design Notes

This document explains the overall design decisions, orchestration, and transformation details.

Orchestration

- The Python CLI acts as the control plane. It validates inputs, loads configuration, maps the CLI-style options to a set of engine arguments, and spawns the Go engine (either a binary or `go run`).
- The Go engine is the data plane and performs deterministic transformations.

Transform order

- Encryption (default): Pig Latin → Caesar cipher.
- Decryption (default): Caesar decipher → Pig Latin deconv.

Tokenization and punctuation strategy (recommended)

- Split tokens into `prefix` (non-letters), `core` (letters and internal apostrophes), and `suffix` (non-letters).
- Transform only `core`. Reattach `prefix` and `suffix` unchanged.
- For hyphenated words, split on `-` and transform components individually.
- Preserve initial capitalization by tracking whether the first rune of `core` is uppercase and reapplying capitalization to the transformed core.

Error handling

- Short-term: the Go engine returns human-readable strings for invalid input. The Python CLI maps those strings to friendly messages in `python_cli/errors.py`.
- Long-term: adopt the `specs/errors.md` typed error codes shared between Python and Go (recommended refactor to typed errors or `(result, Code)` pattern).

Reversibility

- Pig Latin deconv needs either strict rules or minimal metadata to be fully reversible for all tokens. The current approach uses heuristic markers and is good for common cases; add explicit metadata (e.g., markers or an index) if perfect reversibility is required.

Testing strategy

- Keep vector tests in `tests/test_vectors/` so language implementations can consume the same golden data.
- Add round-trip tests (plaintext → encrypt → decrypt → equals plaintext) as the primary acceptance criteria.
