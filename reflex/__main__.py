"""reflex package invocation entry point."""
import sys
import signal
from .reflex import cli


if __name__ == "__main__":
    cli()
