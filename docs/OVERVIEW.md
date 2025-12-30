# Pig Latin + Caesar Cipher — Overview

This repository implements a reversible, learning-focused text transformation tool that composes two deterministic transforms:

- Pig Latin (word-based playful transform)
- Caesar cipher (alphabetic shift)

Purpose

- Educational: practice system design, Go + Python integration, and deterministic reversible transforms.
- Not intended as cryptographic encryption. The aim is controlled obfuscation and deterministic reversibility.

Architecture

- `go-engine/` — core transformation engine written in Go. It contains:
  - `pig_latin` package: forward and reverse Pig Latin functions.
  - `caeser_cypher` package: forward and reverse Caesar cipher functions.
  - `main.go`: a small demo runner.
- `python_cli/` — Python orchestrator and CLI (entry point: `python_cli/main.py`) responsible for:
  - Input validation and configuration.
  - Calling the Go engine (compiled binary or `go run`).
  - Mapping errors into user-friendly messages.
- `specs/` — formal specification documents for Pig Latin, Caesar cipher, pipeline, file rules, and error codes.
- `tests/` — vector-based tests and a `pytest` runner to exercise transformations and round-trips.

Typical flow

1. User runs the Python CLI (`python -m python_cli.main`) with `--input`, `--output`, `--key`, and `--mode`.
2. CLI validates input (encoding, size, simple file rules).
3. CLI calls the Go engine (either an engine binary or `go run ./go-engine`) with mapped arguments.
4. Go performs Pig Latin and Caesar transforms (order depends on encrypt/decrypt mode).
5. CLI writes outputs and reports status.

Design choices

- Use `specs/` as the single source of truth for behavior so both Go and Python implementations match exactly.
- Preserve punctuation and capitalization; transforms operate on alphabetic cores of tokens.
- Use rune-aware processing in Go (recommended) to support Unicode letters.

Where to look next

- `docs/INSTALL.md` — how to set up the environment.
- `docs/USAGE.md` — example CLI commands and expected behavior.
- `go-engine/` — read the implementation and add tests in `go test` or use the Python CLI for orchestration.
