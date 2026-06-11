# Multi-Agent Content Generation Pipeline

A Python-based Multi-Agent AI system that demonstrates how specialized AI agents can collaborate to research, write, and review content automatically using the Groq API and Llama 3.3 70B.

## Overview

This project implements a simple multi-agent architecture where different AI agents are responsible for specific tasks in a content creation workflow.

The pipeline follows this sequence:

Research Agent → Writer Agent → Reviewer Agent

Each agent performs a dedicated role and passes its output to the next stage, creating a complete content generation workflow.

## Features

* Multi-agent architecture
* Research Agent for information gathering
* Writer Agent for article generation
* Reviewer Agent for quality assurance
* Groq API integration
* Environment variable based secret management
* Modular and extensible design
* Git-safe configuration using `.env`

## Project Structure

```text
multi-agent-pipeline/
│
├── my_agents/
│   ├── research_agent.py
│   ├── writer_agent.py
│   └── reviewer_agent.py
│
├── tools/
│   └── search_tools.py
│
├── guardrails/
│   └── quality_checks.py
│
├── groq_config.py
├── run_pipeline.py
├── requirements.txt
├── .env.example
└── README.md
```

## Agent Responsibilities

### Research Agent

* Researches a user-provided topic
* Collects key information
* Produces structured findings

### Writer Agent

* Converts research findings into a well-structured article
* Generates readable and coherent content
* Organizes information logically

### Reviewer Agent

* Evaluates article quality
* Provides feedback
* Improves clarity and consistency
* Produces the final reviewed output

## Technology Stack

* Python 3.11+
* Groq API
* Llama 3.3 70B Versatile
* Pydantic
* python-dotenv

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-pipeline.git

cd multi-agent-pipeline
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Never commit your `.env` file to GitHub.

## Running the Project

```bash
python run_pipeline.py
```

Example workflow:

```text
Input Topic:
"How Multi-Agent AI Systems Are Changing Software Development"

↓ Research Agent

↓ Writer Agent

↓ Reviewer Agent

↓ Final Reviewed Article
```

## Example Use Cases

* AI-powered content generation
* Technical article creation
* Automated report generation
* Multi-agent experimentation
* LLM workflow orchestration

## Future Improvements

* Real web search integration
* Database-backed memory
* Agent-to-agent handoffs
* Advanced guardrails
* Streamlit user interface
* Parallel agent execution
* LangGraph integration

## Security

Sensitive credentials are stored using environment variables and excluded from version control through `.gitignore`.

## License

This project is provided for educational and learning purposes.
