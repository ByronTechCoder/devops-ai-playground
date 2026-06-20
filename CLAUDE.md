# Claude Instructions — devops-ai-playground

This is a monorepo for learning and experimenting with DevOps, AI agent creation, AI development, and coding projects with AI.

## Project Folder Routing

When a user requests a new project, experiment, script, or file, place it in the correct top-level folder based on project type:

| Project Type | Folder | Examples |
|---|---|---|
| DevOps, CI/CD, Docker, Kubernetes, Terraform, Pulumi, Ansible, monitoring, cloud infra | `devops/` | GitHub Actions workflow, Dockerfile, k8s manifest, Terraform module, Prometheus config |
| AI agent, autonomous system, tool-use agent, multi-agent orchestration, LangChain/LangGraph/AutoGen/CrewAI | `ai-agents/` | LLM agent script, tool-calling example, multi-agent pipeline, agent framework demo |
| AI/ML project, fine-tuning, RAG pipeline, embeddings, prompt engineering, AI API integration | `ai-projects/` | OpenAI/Anthropic integration, fine-tune script, RAG notebook, embedding experiment |
| General coding project, web app, CLI tool, automation script, AI-assisted app, third-party integration | `coding-projects/` | Web app with AI features, CLI tool, utility script, API integration |
| Shared documentation, learning notes, architecture diagrams, how-to guides | `docs/` | Architecture notes, tutorial write-ups, reference sheets |

### Sub-folder Guidance

- **`devops/`** → place in the matching sub-folder: `ci-cd/`, `docker/`, `kubernetes/`, `terraform/`, or `monitoring/`
- **`ai-agents/`** → place in: `simple-agent/`, `tool-use/`, `multi-agent/`, or `frameworks/`
- **`coding-projects/`** → place in: `scripts/`, `web-apps/`, `cli-tools/`, or `integrations/`
- **`ai-projects/`** → create a descriptively named sub-folder for each project

## General Conventions

- Every new project or experiment **must** include a `README.md` in its own directory explaining what it does and how to run it.
- Secrets and API keys go in a `.env` file (never committed). Provide a `.env.example` with placeholder values.
- Python projects should use a virtual environment (`python3 -m venv .venv`) and a `requirements.txt`.
- Node.js projects should include a `package.json`.
- Follow the existing style and structure of sibling projects within the same folder.

## When in Doubt

If a project spans multiple categories (e.g., an AI agent deployed with Docker), place it in the folder that best matches the *primary purpose* and note the secondary aspects in the `README.md`.
