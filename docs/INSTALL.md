# Installation

This page describes how to set up a development environment for the project on common platforms (Windows-focused examples are shown). The project uses Go (engine) and Python (CLI/tests).

Prerequisites
- Go toolchain (refer to `go.mod` for the expected version; this repo uses `go 1.25.5`).
- Python 3.10+ (or latest available on your system).

Windows (PowerShell) quick setup
1. Install Go: download and run the Windows MSI from the official Go site, then confirm in PowerShell:

```powershell
go version
```

2. Install Python: use the Windows installer from python.org or the Microsoft Store. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install test and helper packages (optional):

```powershell
python -m pip install --upgrade pip
python -m pip install pytest
```

Linux / macOS brief notes
- Use your platform's package manager to install Go and Python (or download from upstream), then create a venv and install `pytest` as above.

Build and run the Go engine (dev mode)

From the repo root, run:

```powershell
cd go-engine
go run .
```

This runs the demo `main.go` which exercises Pig Latin and Caesar functions.

Build a binary

```powershell
cd go-engine
go build -o ../bin/pig_caesar
```

Now `../bin/pig_caesar` can be used by the Python CLI via `--engine` or `engine_path` in the config.

Notes
- The Python CLI (`python_cli/`) is pure Python and requires only the standard library; `pytest` is optional for running tests.
- If you plan to use Unicode normalization utilities in Go, add `golang.org/x/text` packages to `go.mod`.
