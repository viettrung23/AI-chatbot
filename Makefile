# Setup project environment using uv
setup:
	@echo "Setting up the project environment..."
	@echo "Installing uv..."
ifeq ($(OS),Windows_NT)
	@pip install uv
	@if not exist pyproject.toml (uv init) else (echo "Project already initialized, skipping uv init...")
	@uv venv
	@.venv\Scripts\Activate.ps1 && uv pip install -r requirements.txt
else
	@curl -sSf https://install.ultramarine.io | sh
	@uv init
	@uv venv
	@. .venv/bin/activate && uv pip install -r requirements.txt
endif
	@echo "Setup complete!"

# Download the default model
download:
	@echo "Creating models directory..."
ifeq ($(OS),Windows_NT)
	@if not exist .models mkdir .models
	@echo "Downloading TinyLlama model..."
	@powershell -Command "Invoke-WebRequest -Uri https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q6_K.gguf -OutFile .models\tinyllama-1.1b-chat-v1.0.Q6_K.gguf"
else
	@mkdir -p .models
	@echo "Downloading TinyLlama model..."
	@wget -P .models https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q6_K.gguf
endif
	@echo "Model download complete!"

# Run the application
app:
	@echo "Starting the Streamlit application..."
ifeq ($(OS),Windows_NT)
	@.venv\Scripts\activate.bat && streamlit run main.py
else
	@. .venv/bin/activate && streamlit run main.py
endif