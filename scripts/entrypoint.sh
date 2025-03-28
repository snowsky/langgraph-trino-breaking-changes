#!/bin/bash

if ! command -v curl >/dev/null 2>&1 || ! command -v jq >/dev/null 2>&1; then
    apt-get update && apt-get install -y curl jq && rm -rf /var/lib/apt/lists/*
fi
 
# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo " Retrieve LLAMA3 model..."
ollama pull ${OLLAMA_MODEL_NAME}
echo " Done!"

# Wait for Ollama process to finish.
wait $pid
