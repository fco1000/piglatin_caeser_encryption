# Usage

This document shows common usage patterns for the Python CLI and the Go engine.

Python CLI (recommended orchestration)

Example: encrypt a text file using the Python CLI (PowerShell):

```powershell
python -m python_cli.main -i .\sample_input.txt -o .\encrypted_output.txt -k 7 -m encrypt
```

Example: decrypt using a built engine binary (pass `--engine` or set `engine_path` in config):

```powershell
python -m python_cli.main -i .\encrypted_output.txt -o .\decrypted.txt -k 7 -m decrypt --engine .\bin\pig_caesar
```

Go engine directly (dev mode)

Run the demo in `go-engine`:

```powershell
cd go-engine
go run .
```

Notes on inputs/outputs
- Input files: plain UTF-8 text files (.txt, .md, .json). Binary files are not supported.
- Output: by default the CLI writes the engine stdout to the file specified by `--output`; when using a compiled engine binary that writes files itself, the CLI leaves output handling to the engine.

Testing
- Run the Python vector tests (requires `pytest`):

```powershell
python -m pytest -q
```

Tips
- If the engine is not found, the CLI will attempt to use `go run ./go-engine` so ensure `go` is on your PATH.
- Use the `--config` option to pass a JSON config file with `engine_path` or other overrides.
