#!/usr/bin/env python3
"""Manual Guide CLI - Interactive Q&A for PDF manuals."""

import sys

import click

from pdf_parser import load_pdf
from chat_engine import ChatEngine


def print_help():
    """Print available commands."""
    print("\nCommands:")
    print("  exit, quit  - Exit the application")
    print("  help        - Show this help message")
    print("  reload      - Reload the PDF and clear chat history")
    print("  clear       - Clear conversation history")
    print()


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
def main(pdf_path: str):
    """Interactive Q&A chat for PDF user manuals.

    PDF_PATH: Path to the PDF manual file.
    """
    # Load the PDF
    click.echo(f"Loading manual: {pdf_path}... ", nl=False)
    try:
        doc = load_pdf(pdf_path)
        click.echo(f"done ({doc.total_pages} pages)")
    except Exception as e:
        click.echo(f"error: {e}")
        sys.exit(1)

    # Initialize chat engine
    manual_text = doc.get_full_text()
    engine = ChatEngine(manual_text)

    # Print welcome message
    click.echo("\nManual Guide Ready! Ask questions about the manual.")
    click.echo("Type 'exit' to quit, 'help' for commands.\n")

    # Interactive loop
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            click.echo("\nGoodbye!")
            break

        if not user_input:
            continue

        # Handle commands
        cmd = user_input.lower()
        if cmd in ("exit", "quit"):
            click.echo("Goodbye!")
            break
        elif cmd == "help":
            print_help()
            continue
        elif cmd == "reload":
            click.echo(f"Reloading: {pdf_path}... ", nl=False)
            doc = load_pdf(pdf_path)
            manual_text = doc.get_full_text()
            engine = ChatEngine(manual_text)
            click.echo(f"done ({doc.total_pages} pages)")
            continue
        elif cmd == "clear":
            engine.clear_history()
            click.echo("Conversation history cleared.")
            continue

        # Ask the question
        click.echo("Assistant: ", nl=False)
        engine.ask(user_input)
        click.echo()


if __name__ == "__main__":
    main()
