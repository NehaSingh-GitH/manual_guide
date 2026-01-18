# Manual Guide CLI

An interactive command-line tool that reads PDF user manuals and provides AI-powered Q&A using Claude.

## Features

- PDF text extraction with page number tracking
- Conversational Q&A about manual contents
- Streaming responses for better UX
- Page references in answers
- Conversation history for follow-up questions

## Installation

```bash
git clone https://github.com/NehaSingh-GitH/manual_guide.git
cd manual_guide
pip install -r requirements.txt
```

## Usage

Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY=your-api-key
```

Run with a PDF manual:
```bash
python3 main.py path/to/manual.pdf
```

### Commands

| Command | Description |
|---------|-------------|
| `help`  | Show available commands |
| `clear` | Clear conversation history |
| `reload`| Reload the PDF file |
| `exit`  | Quit the application |

## Example

```
$ python3 main.py sample_manual.pdf
Loading manual: sample_manual.pdf... done (4 pages)

Manual Guide Ready! Ask questions about the manual.
Type 'exit' to quit, 'help' for commands.

You: How do I reset my password?
Assistant: According to page 3, to reset your password:
1. Go to Settings > Security > Password
2. Click "Forgot Password"
3. Enter your registered email address
4. Check your email for a reset link
5. Create a new password (minimum 8 characters)

You: exit
Goodbye!
```

## Requirements

- Python 3.10+
- Anthropic API key

## License

MIT
