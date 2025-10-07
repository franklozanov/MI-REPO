"""Command line entry point for the migrated MI-REPO project."""

from __future__ import annotations

import argparse

from src.mi_repo.app import main as generate_greeting


def parse_args() -> argparse.Namespace:
    """Parse command line arguments for the greeting generator."""

    parser = argparse.ArgumentParser(
        description=(
            "Generate a friendly greeting to confirm the project works after "
            "being migrated from Replit."
        )
    )
    parser.add_argument(
        "--name",
        default="world",
        help="Optional name that will appear in the greeting (defaults to 'world').",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point that prints the generated greeting."""

    args = parse_args()
    print(generate_greeting(args.name))


if __name__ == "__main__":  # pragma: no cover - allows running as a script
    main()
