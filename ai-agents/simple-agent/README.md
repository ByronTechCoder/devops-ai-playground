# Simple Agent

A minimal "hello world" AI agent to get started with LLM-powered agents.

## What it does

This agent accepts a user prompt and responds using the OpenAI Chat Completions API. It demonstrates the basic loop of:

1. Receiving user input
2. Sending it to an LLM
3. Returning the response

## Requirements

- Python 3.9+
- An OpenAI API key

## Setup

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

```bash
python agent.py "What is the capital of France?"
```

## Next Steps

Once comfortable with this basic example, explore:
- `../tool-use/` — Add tools the agent can call
- `../multi-agent/` — Coordinate multiple agents
