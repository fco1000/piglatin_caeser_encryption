# Pig Latin Test Plan

This file documents the Pig Latin tests included in `tests/test_vectors` and exercised by `tests/test_pipeline.py`.

Key points:
- Vowel-starting words append `way` (e.g., `apple` → `appleway`).
- Consonant-starting words move leading consonant cluster to the end and append `ay` (e.g., `chair` → `airchay`).
- Capitalization is preserved: the transformed word keeps initial capitalization when applicable.
- Punctuation attached to words is preserved in position (e.g., `Hello!` → `Ellohay!`).
- Hyphenated words are split on `-` and each component transformed separately.

Notes on tests:
- Tests are intentionally "best-effort" to follow the specification in `specs/Pig_latin.md`.
- `pig_latin_deconv` in the test runner uses a heuristic reversal approach—sufficient for test vectors but not a production-grade reversal.
- The JSON files in `tests/test_vectors/` contain the input and expected Pig Latin outputs.

If you want a different Pig Latin variant (for example using `yay` for vowels), update the vectors and the `pig_latin_token` implementation in `tests/test_pipeline.py`.
