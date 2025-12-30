import argparse
from typing import Optional


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="pigcipher", description="Pig Latin + Caesar cipher CLI (Python orchestrator)")
    p.add_argument("-i", "--input", required=True, help="Input file path (plain text)")
    p.add_argument("-o", "--output", required=True, help="Output file path")
    p.add_argument("-k", "--key", required=True, type=int, help="Caesar shift key (integer)")
    p.add_argument("-m", "--mode", choices=("encrypt", "decrypt"), default="encrypt", help="Mode: encrypt or decrypt")
    p.add_argument("--engine", default=None, help="Path to Go engine binary. If omitted, uses `go run ./go-engine` when available.")
    p.add_argument("--config", default=None, help="Optional config file (JSON) to override defaults")
    return p


def parse_args(args: Optional[list] = None):
    parser = build_parser()
    return parser.parse_args(args)
