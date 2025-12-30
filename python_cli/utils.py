import os
from pathlib import Path
from typing import Tuple


def path_exists(path: str) -> bool:
    return os.path.exists(path)


def is_text_file(path: str) -> bool:
    """Simple check to allow .txt/.md/.json per project file rules."""
    ext = Path(path).suffix.lower()
    return ext in {".txt", ".md", ".json"}


def file_size_ok(path: str, max_bytes: int) -> bool:
    try:
        return os.path.getsize(path) <= max_bytes
    except OSError:
        return False


def ensure_input_valid(path: str, max_bytes: int) -> Tuple[bool, str]:
    if not path_exists(path):
        return False, "input file not found"
    if not is_text_file(path):
        return False, "unsupported file type; use .txt/.md/.json"
    if not file_size_ok(path, max_bytes):
        return False, "input file too large"
    return True, "ok"
