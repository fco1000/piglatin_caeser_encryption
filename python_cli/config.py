import json
import os
from typing import Dict, Any

# Default configuration for the CLI and engine mapping
DEFAULT_CONFIG: Dict[str, Any] = {
    "engine_path": None,  # if None, runner may use 'go run ./go-engine'
    "max_input_size": 5 * 1024 * 1024,  # 5 MB default
}


def load_config(path: str | None) -> Dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if not path:
        return cfg
    if not os.path.exists(path):
        raise FileNotFoundError(f"config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    cfg.update(data or {})
    return cfg


def map_to_engine_args(mode: str, input_path: str, output_path: str, key: int, cfg: Dict[str, Any]) -> list:
    """Map CLI args to Go engine args.

    The engine in this repo doesn't yet implement a flags interface; the runner will
    either call a compiled binary or `go run`. This helper centralizes how args
    would be passed once the engine supports CLI flags.
    """
    # Using named flags is future-proof. Adjust as engine flags evolve.
    return [
        f"--mode={mode}",
        f"--input={input_path}",
        f"--output={output_path}",
        f"--key={int(key)}",
    ]
