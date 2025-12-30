from typing import Dict

# Map known engine messages / error keys to user-friendly messages.
# The Go engine currently returns plain strings; when it moves to structured
# error codes, map them here.

ERROR_MAP: Dict[str, str] = {
    "enter valid input": "Invalid input provided to engine",
    "enter valid key value above 1 but below 25": "Invalid Caesar key: must be 1..25",
    "Enter valid input value": "Invalid input provided to engine",
    "Enter valid key value": "Invalid Caesar key",
}


def friendly_message(raw: str) -> str:
    if not raw:
        return ""
    raw_str = raw.strip()
    for k, v in ERROR_MAP.items():
        if k in raw_str:
            return v
    # default fallback
    return raw_str
