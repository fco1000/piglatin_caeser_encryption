# Pipeline: Encrypt → Decrypt (Pig Latin + Caesar cipher)

Purpose
- Define ordered stages for encrypting then decrypting text using Pig Latin + Caesar cipher.
- Specify inputs/outputs, failure modes, and recommended error handling.

Assumptions
- Plain UTF-8 text input.
- Caesar shift is an integer key (positive or negative).
- Pig Latin rules: word-based transform (configurable for punctuation/capitalization).
- Binary-safe packaging (e.g., base64) used for transport/storage.
- Optional checksum or signature for tamper detection.

## High-level flow
1. Encrypt pipeline
    1. Validate input
    2. Normalize text
    3. Pig Latin transform
    4. Caesar cipher shift (use provided key)
    5. Package (encode + optional checksum)
    6. Emit encrypted artifact

2. Decrypt pipeline (reverse)
    1. Validate artifact
    2. Unpackage (decode + checksum verify)
    3. Caesar cipher unshift (use same key)
    4. Reverse Pig Latin transform
    5. Denormalize (restore capitalization/punctuation)
    6. Emit plaintext

## Stage details

- Stage: Validate input
  - Input: raw string or file
  - Output: validated payload or error
  - Failure: empty input, unsupported encoding → return 400 / E_INVALID_INPUT
  - Handling: reject with clear message, log reason

- Stage: Normalize text
  - Input: validated string
  - Output: normalized tokens (preserve metadata for punctuation/case)
  - Failure: normalization error → E_NORMALIZE
  - Handling: fail fast; optionally continue with best-effort normalization if configured

- Stage: Pig Latin transform
  - Input: normalized tokens
  - Output: transformed tokens
  - Failure: unexpected token type → E_PIGLATIN
  - Handling: log token skip; if policy strict → abort

- Stage: Caesar cipher shift
  - Input: transformed text and key
  - Output: shifted bytes/string
  - Failure: missing/invalid key → E_BAD_KEY
  - Handling: return explicit error; do not proceed without valid key

- Stage: Package (encode + checksum)
  - Input: shifted output
  - Output: base64 or container with checksum/signature
  - Failure: encoding error → E_PACKAGE
  - Handling: abort and log; avoid emitting partial artifacts

- Stage: Emit encrypted artifact
  - Output: file/stdout/object ready for storage or transport
  - Metadata must include algorithm and key identifier (not key)

Reverse stages mirror above; include checksum verification after unpacking.

## Error handling & codes (recommended)
- E_INVALID_INPUT — invalid or empty input
- E_NORMALIZE — normalization failed
- E_PIGLATIN — pig latin transform failure
- E_BAD_KEY — missing/invalid Caesar key
- E_CRYPTO — shift/encoding errors
- E_PACKAGE — encode/decode packaging errors
- E_CHECKSUM — checksum/signature mismatch (possible tampering)
- E_INTERNAL — unexpected runtime error

Behavior on error
- Deterministic: return error code + human-readable message
- Fail-fast for fatal errors (invalid input, bad key, checksum mismatch)
- Recoverable errors (e.g., non-critical token skips): continue with warning if configured
- Logging: include stage name, error code, input identifier (not sensitive data), and trace id
- Metrics: count per error type and stage

## Security & integrity
- Never store raw keys with artifacts; reference a key ID.
- Always verify checksum/signature during decrypt; treat mismatch as fatal.
- Sanitize logs to avoid leaking plaintext or keys.
- Use authenticated packaging (HMAC or signature) where possible.

## Examples (expected outputs)
- Success: exit 0, body = base64-encoded artifact or file path
- Checksum mismatch: exit 3, message = "E_CHECKSUM: artifact integrity failed"
- Missing key: exit 2, message = "E_BAD_KEY: Caesar key required"

## Tests to include
- Round-trip test: plaintext → encrypt → decrypt → equals plaintext
- Invalid key test: decrypt with wrong key → E_CHECKSUM or incorrect plaintext (detectable)
- Empty input test → E_INVALID_INPUT
- Punctuation/case preservation test

Notes
- Keep transforms deterministic and reversible.
- Document Pig Latin variant used and Caesar normalization (alphabet wrap, non-letters handling).
