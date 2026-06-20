# DevOps

This section contains DevOps experiments, pipelines, and infrastructure-as-code projects.

## Topics Covered

- **CI/CD** — GitHub Actions workflows, pipeline design patterns
- **Containers** — Docker and Docker Compose setups
- **Orchestration** — Kubernetes manifests and Helm charts
- **Infrastructure as Code** — Terraform, Pulumi, or Ansible playbooks
- **Monitoring & Observability** — Prometheus, Grafana, logging stacks
- **Cloud** — AWS, GCP, or Azure experiments

## Directory Layout

```
devops/
├── ci-cd/          # CI/CD pipeline examples
├── docker/         # Dockerfile and Docker Compose examples
├── kubernetes/     # K8s manifests and Helm charts
├── terraform/      # Infrastructure as code
└── monitoring/     # Observability and monitoring setups
```

## Getting Started

Browse to any subdirectory and follow the `README.md` within it. Most experiments will require:

- Docker / Docker Desktop
- `kubectl` + a local cluster (e.g., kind, minikube) for Kubernetes experiments
- Terraform CLI for IaC experiments
- A cloud account (AWS Free Tier, GCP Free Tier, etc.) where applicable
