"""AI-powered Q&A chat engine using Claude."""

import os
import sys

from anthropic import Anthropic


class ChatEngine:
    """Handles AI-powered Q&A about a manual."""

    SYSTEM_PROMPT = """You are a helpful assistant that answers questions about a user manual.
You have been provided with the full text of the manual below.

When answering questions:
- Reference specific page numbers when relevant (e.g., "According to page 5...")
- Be concise but thorough
- If the answer isn't in the manual, say so clearly
- Quote relevant sections when helpful

Manual content:
{manual_text}
"""

    def __init__(self, manual_text: str):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("Error: ANTHROPIC_API_KEY environment variable not set.")
            print("Please set it with: export ANTHROPIC_API_KEY=your-key")
            sys.exit(1)

        self.client = Anthropic(api_key=api_key)
        self.manual_text = manual_text
        self.conversation_history: list[dict] = []

    def _get_system_prompt(self) -> str:
        """Build the system prompt with manual context."""
        return self.SYSTEM_PROMPT.format(manual_text=self.manual_text)

    def ask(self, question: str) -> str:
        """Ask a question and get a streamed response."""
        self.conversation_history.append({
            "role": "user",
            "content": question
        })

        response_text = ""

        with self.client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=self._get_system_prompt(),
            messages=self.conversation_history
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                response_text += text

        print()  # Newline after streaming

        self.conversation_history.append({
            "role": "assistant",
            "content": response_text
        })

        return response_text

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
