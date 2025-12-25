# Piglatin/ Caeser cypher encryption

## Title

Pig Latin plus Caesar Cipher File Transformer
Python and Go Hybrid Project

## Overview

This project is a learning focused file transformation tool.
It combines Pig Latin text transformation and a Caesar cipher shift.
It is not secure encryption. It is controlled obfuscation.

The project uses two languages.
Go handles all transformation logic.
Python handles user interaction and orchestration.

### Goals

- Practice clean system design
- Learn cross language integration
- Enforce strict specs across implementations
- Build reversible text transformations

### Non Goals

- Strong cryptography
- Data security against attackers
- Production grade encryption

## How It Works

### Encryption flow

1. Python validates input and arguments
2. Python calls the Go engine
3. Go applies Pig Latin
4. Go applies Caesar cipher
5. Output is written to file

### Decryption flow

1. Python validates encrypted file
2. Python calls the Go engine
3. Go reverses Caesar cipher
4. Go reverses Pig Latin
5. Original text is restored

## Language Responsibilities

#### Go

- Core transformation engine
- Pig Latin forward and reverse
- Caesar cipher forward and reverse
- File safe processing
- Deterministic output

#### Python

- Command line interface
- Argument parsing
- Config handling
- Input validation
- Error reporting
- Calling Go binary

## Project Structure

root
- spec (Contains all transformation rules and edge cases)
- go_engine (Go source code for the transformation engine)
- python_cli (Python CLI that users interact with)
- tests (Cross language tests to ensure identical behavior)
- docs(Design notes and explanations)

Specification First Rule

All behavior is defined in spec files.
Both Python and Go must follow the spec exactly.
If output differs, the implementation is wrong.

#### Pig Latin Rules

Pig Latin is deterministic.
Punctuation and spacing are preserved.
Reverse transformation is supported by strict rules or metadata.

#### Caesar Cipher Rules

Alphabet only shifting.
Uppercase and lowercase preserved.
Non alphabet characters untouched.
Shift value is configurable.

### Limitations

- Not secure encryption
- Large binary files not supported
- Reverse Pig Latin requires strict rules

### Why Python plus Go

Python
- Fast iteration
- Clean CLI
- Easy validation

Go
- Speed
- Strong typing
- Single binary engine

This split keeps the project clean and maintainable.

Intended Audience

- Students
- Developers learning Go
- Developers learning system design
- Anyone practicing reversible transformations

Future Extensions

- GUI wrapper
- Metadata based Pig Latin reversal
- Streaming large files
- Additional ciphers
