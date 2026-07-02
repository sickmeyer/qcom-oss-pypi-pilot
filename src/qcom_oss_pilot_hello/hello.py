"""Core logic for the pilot hello package."""

from __future__ import annotations


def greet(name: str = "World") -> str:
    """Return a greeting string.

    Args:
        name: The name to greet.  Defaults to ``"World"``.

    Returns:
        A greeting of the form ``"Hello, <name>!"``.

    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("PyPI")
        'Hello, PyPI!'
    """
    return f"Hello, {name}!"


def main() -> None:
    """Entry-point for the ``qcom-hello`` console script."""
    print(greet())


if __name__ == "__main__":
    main()
