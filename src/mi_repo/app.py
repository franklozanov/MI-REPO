"""Simple application module used after migrating from Replit."""

from __future__ import annotations


def build_greeting(name: str) -> str:
    """Return a friendly greeting for *name*.

    The function is intentionally tiny so new contributors can quickly verify the
    project works outside of Replit.
    """

    clean_name = name.strip() or "world"
    return f"Hello, {clean_name}! Welcome to the migrated MI-REPO project."


def main(name: str = "world") -> str:
    """Return the greeting used by the command line entry point."""

    return build_greeting(name)
