# AI Agents

This section contains projects and experiments focused on building AI agents — autonomous systems that can reason, plan, use tools, and accomplish complex tasks.

## Topics Covered

- **LLM-powered agents** — Agents built on top of OpenAI, Anthropic, or open-source LLMs
- **Tool use / Function calling** — Giving agents the ability to call external tools and APIs
- **Multi-agent systems** — Coordinating multiple agents to work together
- **Memory & persistence** — Short-term and long-term memory for agents
- **Frameworks** — LangChain, LangGraph, AutoGen, CrewAI, etc.

## Directory Layout

```
ai-agents/
├── simple-agent/        # A minimal "hello world" agent example
├── tool-use/            # Agents with external tool integrations
├── multi-agent/         # Multi-agent orchestration experiments
└── frameworks/          # Framework-specific examples and comparisons
```

## Getting Started

Most projects in this section are Python-based. General prerequisites:

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` in the project folder and add your API keys before running.
