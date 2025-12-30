import shutil
import subprocess
import sys
from typing import Tuple, List, Optional


def find_go() -> Optional[str]:
    return shutil.which("go")


def run_engine(engine_path: Optional[str], engine_args: List[str], cwd: Optional[str] = None) -> Tuple[int, str, str]:
    """Run the Go engine.

    If `engine_path` is provided and is executable, it will be executed directly.
    Otherwise the function will attempt to run `go run ./go-engine` (requires `go`).

    Returns: (returncode, stdout, stderr)
    """
    if engine_path:
        cmd = [engine_path] + engine_args
    else:
        go_bin = find_go()
        if not go_bin:
            return 127, "", "go tool not found in PATH and no engine binary provided"
        # run the package directory so the engine's main.go runs
        cmd = [go_bin, "run", "./go-engine"] + engine_args

    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)
        return proc.returncode, proc.stdout or "", proc.stderr or ""
    except FileNotFoundError as e:
        return 127, "", str(e)
    except Exception as e:
        # unexpected
        return 1, "", str(e)


def make_engine_cmdline(engine_path: Optional[str], engine_args: List[str]) -> str:
    base = engine_path if engine_path else "go run ./go-engine"
    return " " .join([base] + engine_args)


if __name__ == "__main__":
    print("This module provides runner.run_engine() for the CLI.")
