# Caesar cipher

A Caesar cipher is a simple substitution cipher that shifts each letter in the plaintext by a fixed number (the key) through the alphabet. It was famously used by Julius Caesar.

## How it works (algorithm)
- Choose a shift key $k$ (commonly $0 \le k \le 25$).
- For each alphabetic character, convert it to a 0–25 index (A/a = 0, B/b = 1, ... Z/z = 25).
- Compute the shifted index and wrap around using modulo 26.
  $$C = (P + k) \bmod 26$$
  where $P$ is the plaintext index and $C$ is the ciphertext index.
- To decrypt:
  $$P = (C - k) \bmod 26$$
- Preserve letter case (uppercase stays uppercase, lowercase stays lowercase).
- Non-letter characters (spaces, punctuation, numbers) are left unchanged.

## Rules
- Key values are integers; $k$ and $k \bmod 26$ are equivalent (e.g., $k=27$ ≡ $k=1$).
- Negative keys perform left shifts (e.g., $k=-3$).
- Only alphabetic characters are shifted; other characters remain as-is.
- Caesar cipher is not secure by modern standards — brute force requires checking only 26 keys.

## Short examples
- Shift $k=3$ (classic example):
  - Plain: `HELLO` → Cipher: `KHOOR`
- Lowercase preserved:
  - Plain: `hello` → Cipher: `ifmmp` (with $k=1$)
- Non-letters unchanged:
  - Plain: `Attack at dawn!` → Cipher (with $k=5`): `Fyyfhp fy ifbs!`
- Decrypting:
  - Cipher: `KHOOR` with $k=-3$ → Plain: `HELLO`

## Quick implementation note
- Implementations typically map chars to code points, apply the shift within `'A'..'Z'` or `'a'..'z'`, then convert back.
- Be careful with Unicode alphabets or accented characters — Caesar is defined for the basic Latin alphabet only.