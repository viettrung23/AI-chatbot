import os
from dotenv import load_dotenv

class Config:
    """Configuration class for model parameters."""
    load_dotenv()  # Load environment variables from .env file
    MODEL_ID = os.getenv("MODEL_ID", "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF")
    MODEL_PATH = os.getenv("MODEL_PATH", ".models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf")
    MAX_TOKENS = 768
    TEMPERATURE = 0.22
    TOP_P = 0.95
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
    system_prompt = (
        """
            You are a helpful assistant that can answer questions in two ways:
    
            1. For general knowledge questions, answer directly using your knowledge.
            
            2. For specific information about weather, use the ReAct style (Thought / Action / Observation / Final Answer) with the following tool:
    

            get_weather: Get the current weather for a location.
            Usage example:
            {
            "action": "get_weather",
            "action_input": {"location": "New York"}
            }

            You must always follow **exactly** this format:

            Question: What is the weather in New York?
            Thought: I need to check the weather in New York.
            Action:
            ```json
            {
                "action": "get_weather",
                "action_input": {"location": "New York"}
            }
            Observation: It's currently sunny with a temperature of 25°C. 
            Thought: I now know the final answer. 
            Final Answer: The weather in New York is sunny with a temperature of 25°C.
            Now answer the following question in the exact same format, and only use a single action per step.
        """
    )
