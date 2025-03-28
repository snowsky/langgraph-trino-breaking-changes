# Trino Breaking Changes Analyzer

## Overview

This project uses AI to analyze Trino release notes and identify breaking changes between different versions. It combines several components:

## Architecture

The system consists of multiple services:

- **Ollama**: Runs the local LLM for text summarization
- **Backend**: FastAPI service for web scraping
- **Agent**: Main analysis service using LangGraph
- **Gradio UI**: Web interface for user interactions

## Prerequisites

- Docker and Docker Compose
- Python 3.13
- At least 16GB RAM recommended for running the LLM

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/snowsky/langgraph-trino-breaking-changes.git
cd langgraph-trino-breaking-changes
```

2. Update environment variables for start and end versions:

```
cp .env.example .env
# Edit .env file or docker-compose.yaml file
```

2. Start all services using Docker Compose and see live logs:

```bash
docker-compose up --build
```

This will start:
- Ollama LLM service on port 11434
- Ollama Web UI on port 8080 (accessible at [http://localhost:8080](http://localhost:8080))
- Backend service on port 8000
- Agent service for analysis

## Manual Setup

If you prefer to run services separately:

1. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r my_agent/requirements.txt
```

3. Start the backend service:

```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Start the Gradio interface:

```bash
pip install -r gradio/requirements.txt
python gradio/gradio_trino_changes.py
```

Once the Gradio interface is running, open your browser and navigate to [http://localhost:7860](http://localhost:7860) to access the UI. After each analysis run, you can copy the results directly from the interface for further use.

## Test drive

```
python run_agent.py
```

## Output files

Example summary and markdown files can be found under `output` folder.

## Environment Variables

Key environment variables (configured in docker-compose.yaml):

```
COLLECTION_NAME=my_collection
BACKEND_CRAWLSVC_URL=http://backend:8000 
TRINO_RELEASE_URL=https://trino.io/docs/current/release.html
OLLAMA_MODEL_NAME=llama3.2
OLLAMA_BASE_URL=http://ollama:11434
OLLAMA_NUM_CTX=8192
```

## Project Structure

```
├── backend/               # FastAPI web scraping service
├── gradio/                # Gradio web interface
├── my_agent/              # Main analysis logic
├── ollama/                # Ollama model configurations
└── docker-compose.yaml    # Service orchestration
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is Apache licensed.
