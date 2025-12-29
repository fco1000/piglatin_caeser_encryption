# Caesar Cipher Test Plan

This file documents the Caesar cipher tests used by `tests/test_pipeline.py`.

Key points:

- Only basic Latin letters are shifted; case is preserved.
- Non-letter characters (digits, punctuation, whitespace) remain unchanged.
- Shift (`k`) normalizes modulo 26; negative shifts are allowed and equivalent to left shifts.
- Tests include forward and reverse checks: applying the cipher and then the decipher should restore the original.

Notes on tests:

- The JSON vectors include `caesar_key` and `caesar_expected` for forward-check assertions.
- The `caesar_decipher` test ensures round-trip correctness.
