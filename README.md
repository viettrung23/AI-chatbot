# Basic AI Agent with llama-cpp-python and Streamlit

A simple Streamlit-based chatbot using llama-cpp-python to run LLM models locally.

## Setup

### Using Makefile (Recommended)

The project includes a Makefile that works on both Windows and Unix-based systems. You can use it to quickly set up and run the project:

```bash
# Setup the environment (installs uv and dependencies)
make setup

# Download the default TinyLlama model
make download

# Run the application
make app
```

## Usage

1. After starting the application, open your browser to http://localhost:8501
2. Enter your question in the chat input at the bottom of the page
3. The AI will process your question and provide a response
4. Your conversation history will be preserved during the session

## Configuration

You can configure the model by editing the `.env` file:
- `MODEL_ID`: The model ID from Hugging Face (used for reference only)
- `MODEL_PATH`: The GGUF model filename in the `.models` directory

Advanced settings can be modified in `config.py`:
- `MAX_TOKENS`: Maximum number of tokens in the AI response (default: 256)
- `TEMPERATURE`: Controls randomness of responses (default: 0.7)
- `TOP_P`: Controls diversity of responses (default: 0.95)

## Choosing Different Models

For better performance, you can use larger models:

- [Mistral 7B Instruct](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
- [Llama 2 13B Chat](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF)
- [Vicuna 13B](https://huggingface.co/TheBloke/vicuna-13B-v1.5-GGUF)

When downloading larger models, choose an appropriate quantization based on your hardware:
- Q4_K, Q5_K: Lower memory usage, slightly lower quality
- Q6_K, Q8_K: Higher memory usage, better quality
