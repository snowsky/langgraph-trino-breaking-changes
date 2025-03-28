import os

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Backend configuration (used by load_page_contents)
BACKEND_CRAWLSVC_URL = os.getenv("BACKEND_CRAWLSVC_URL", "http://localhost:8000")
TRINO_RELEASE_URL = os.getenv("TRINO_RELEASE_URL", "https://trino.io/docs/current/release.html")

# Ollama model configuration
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3.2")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_NUM_CTX = int(os.getenv("OLLAMA_NUM_CTX", "8192"))
