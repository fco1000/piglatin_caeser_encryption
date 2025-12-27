# File rules

This document defines allowed file types, encoding, and line-ending rules for the Pig Latin + Caesar cipher encryption tool.

## Allowed file types
- Plain text files only.
    - Allowed extensions: `.txt`, `.md`, `.json`
    - Files must contain human‑readable text. Binary files (images, archives, executables) are not allowed.
- Single-file inputs only. If multiple files are required, use an archive that complies with the encoding rules and is validated before processing.

## Encoding rules
- Required encoding: UTF-8 (without BOM) recommended.
    - Incoming files encoded with UTF-8 with BOM are accepted but BOM is removed before processing.
    - Files not encoded in UTF-8 should be rejected with a clear error message instructing the user to convert to UTF-8.
- Unicode normalization: normalize to NFC before processing.
- Character handling:
    - Transformations (Pig Latin and Caesar cipher) apply only to alphabetic characters.
    - Alphabetic characters: Unicode letters (General Category "L") are supported.
    - Case is preserved: uppercase stays uppercase; lowercase stays lowercase.
    - Non-letter characters (digits, punctuation, symbols, whitespace) are preserved in place and are not shifted.
- Charset limits: control and non‑printing characters (except standard whitespace: space, tab, newline) must be removed or cause rejection.

## Line ending rules
- Canonical repository line ending: LF (`\n`).
- Accepted inputs:
    - Files with LF (`\n`) — processed as-is.
    - Files with CRLF (`\r\n`) — accepted, normalized to LF before processing.
    - Files with lone CR (`\r`) — treated as LF equivalents for compatibility.
- Output files: always written with LF line endings. If a client needs CRLF, perform conversion as a post‑processing step.

## File size and performance
- Maximum file size: 5 MB by default. Larger files must be split or processed using a streaming mode.
- For streaming mode, adhere to the same encoding and line ending rules on each chunk boundary.

## Validation and error responses
- If a file fails validation, return an error with:
    - HTTP/CLI code (e.g., 400 Bad Request).
    - Short reason (e.g., "Unsupported encoding").
    - Suggested fix (e.g., "Convert file to UTF-8 without BOM and normalize line endings to LF").
- Common error conditions:
    - Unsupported extension or binary content → "Unsupported file type".
    - Non‑UTF-8 encoding → "Unsupported encoding — convert to UTF-8".
    - Contains disallowed control characters → "File contains invalid control characters".

## Examples
- Accepted: `notes.txt` encoded UTF-8, LF endings, contains letters, digits, punctuation.
- Rejected: `image.png` (binary), `oldfile.txt` encoded in ISO-8859-1 (unless converted).

## Implementation notes
- Normalize encoding and line endings as the first preprocessing step.
- Validate file size and character set before applying Pig Latin or Caesar transformations.
- Document in the CLI/API help the exact rules and a sample conversion command for Windows users (how to convert CRLF→LF and encodings).
