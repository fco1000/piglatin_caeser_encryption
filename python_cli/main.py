import sys
import logging

from .args import parse_args
from .config import load_config, map_to_engine_args
from .utils import ensure_input_valid
from .runner import run_engine
from .errors import friendly_message


logger = logging.getLogger("pigcipher")


def main(argv=None):
    args = parse_args(argv)

    # load config (if any)
    cfg = load_config(args.config)

    ok, reason = ensure_input_valid(args.input, cfg.get("max_input_size", 5 * 1024 * 1024))
    if not ok:
        logger.error("Input validation failed: %s", reason)
        sys.exit(2)

    engine_args = map_to_engine_args(args.mode, args.input, args.output, args.key, cfg)

    code, out, err = run_engine(cfg.get("engine_path"), engine_args, cwd=None)

    if code != 0:
        friendly = friendly_message(err or out)
        logger.error("Engine failed (code=%s): %s", code, friendly)
        # print raw outputs for debugging
        if out:
            logger.debug("engine stdout: %s", out)
        if err:
            logger.debug("engine stderr: %s", err)
        sys.exit(code if code != 127 else 3)

    # success: write stdout to output file if engine printed transformed text
    if out:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(out)
        except Exception as e:
            logger.error("Failed writing output: %s", e)
            sys.exit(4)

    print("Operation completed successfully.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
