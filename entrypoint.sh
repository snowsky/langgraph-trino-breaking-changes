#!/bin/bash

apt update && apt install -y curl
 
# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo " Retrieve LLAMA3 model..."
ollama pull ${OLLAMA_EMBEDDINGS_MODEL}
ollama pull ${OLLAMA_MODEL_NAME}
echo " Done!"

# Wait for Ollama process to finish.
wait $pid
