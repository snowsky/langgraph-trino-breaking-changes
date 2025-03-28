from langchain_ollama import ChatOllama
from my_agent.config import OLLAMA_MODEL_NAME, OLLAMA_BASE_URL, OLLAMA_NUM_CTX

def create_llm_model():
    """Create and configure the LLM model"""
    return ChatOllama(
        model=OLLAMA_MODEL_NAME,
        base_url=OLLAMA_BASE_URL,
        num_ctx=OLLAMA_NUM_CTX
    )
