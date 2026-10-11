# Portfolio AgentCore MCP server

This project was created with the [AgentCore CLI](https://github.com/aws/agentcore-cli).

## 💻 Technologies

| **Category**                  | **Technology**                                     |
| ----------------------------- | -------------------------------------------------- |
| **mcp**                       | Python (mcp package) https://pypi.org/project/mcp/ |
| **_cv search tool_**          | AWS S3 + Bedrock knowledgebase + Pinecone          |
| **_cv github projects tool_** | Github API                                         |
| **Agent**                     | https://github.com/mrobert3456/portfolio_agent     |
| **Infrastructure**            | AWS Agentcore (MCP server, Strands agent, gateway) |
| **CI/CD**                     | Github actions                                     |

## ⚙ Project Structure

```
my-project/
├── AGENTS.md               # AI coding assistant context
├── agentcore/
│   ├── agentcore.json      # Project config (agents, memories, credentials, gateways, evaluators)
│   ├── aws-targets.json    # Deployment targets (account + region)
│   ├── .env.local          # Secrets — API keys (gitignored)
│   ├── .llm-context/       # TypeScript type definitions for AI assistants
│   │   ├── agentcore.ts    # AgentCoreProjectSpec types
│   │   ├── aws-targets.ts  # Deployment target types
│   │   └── mcp.ts          # Gateway and MCP tool types
│   └── cdk/                # CDK infrastructure (@aws/agentcore-cdk)
├── app/                    # Agent application code
└── evaluators/             # Custom evaluator code (if any)
```

## 🚀 Installation

### Prerequisites

- **Node.js** 20.x or later
- **Python 3.10+** and **uv** for Python agents ([install uv](https://docs.astral.sh/uv/getting-started/installation/))
- **AWS credentials** configured (`aws configure` or environment variables)
- **Docker** (only for Container build agents)

1. Download this repository by running:

```
git clone https://github.com/mrobert3456/portfolio_mcp.git
cd portfolio_mcp/app/portfoliomcp
```

2. Install dependencies by running:

```
uv sync
```

3. Start development server by running:

```
agentcore dev
```

## ⚡ CI/CD pipeline

This application is deployed to AWS using a CI/CD pipeline created with **Github Actions**.
