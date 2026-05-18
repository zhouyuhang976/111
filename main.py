from __future__ import annotations

import argparse
from pathlib import Path

from bot.config import load_config
from bot.engine import TradingEngine


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Binance spot quant bot")
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to config JSON file",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run a single decision cycle and exit",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = Path(args.config).resolve()
    config = load_config(config_path)
    engine = TradingEngine(config=config, config_path=config_path)
    if args.once:
        engine.run_once()
    else:
        engine.run_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
