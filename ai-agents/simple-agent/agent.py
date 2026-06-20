"""
Simple AI Agent — a minimal example using the OpenAI Chat Completions API.

Usage:
    python agent.py "Your prompt here"
"""

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def run_agent(prompt: str) -> str:
    """Send a prompt to the LLM and return the response."""
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python agent.py \"<your prompt>\"")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    print(f"Prompt: {prompt}\n")

    reply = run_agent(prompt)
    print(f"Agent: {reply}")


if __name__ == "__main__":
    main()
