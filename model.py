from llama_cpp import Llama
import re
import json
from common.config import Config
from tools.get_weather import get_weather

class LLM:
    def __init__(self, config: Config):
        self.config: Config = config
        self.model = Llama(
            model_path=self.config.MODEL_PATH,
            n_ctx=2048,
            n_batch=512,
            verbose=False
        )
        self.max_tokens = config.MAX_TOKENS
        self.temperature = config.TEMPERATURE
        self.top_p = config.TOP_P
        self.system_prompt = config.system_prompt
    
    def extract_action_from_response(self, text: str):
        json_match = re.search(r'```json\s*(.*?)(?:```|$)', text, re.DOTALL)

        if json_match:
            json_text = json_match.group(1).strip()
            
            # Parse JSON
            try:
                data = json.loads(json_text)
                
                # Lấy action và action_input
                action = data["action"]
                action_input = data["action_input"]
                
                return action, action_input
            except json.JSONDecodeError as e:
                print(f"Lỗi khi parse JSON: {e}")
        else:
            print("Không tìm thấy dữ liệu JSON trong đoạn text")

        return None, None

    def generate(
        self,
        prompt: str,
        max_tokens: int = None,
        temperature: float = None,
        top_p: float = None,
        tools: list = None,
    ) -> str:
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens
        temperature = temperature if temperature is not None else self.temperature
        top_p = top_p if top_p is not None else self.top_p
        tools = [get_weather]

        current_prompt = (
            f"<|start|>\n"
            f"<|system|>\n{self.system_prompt.strip()}\n"
            f"<|user|>\nQuestion: {prompt.strip()}\n"
            f"<|assistant|>\n"
        )

        response = self.model(
            current_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=["Observation:"],
            echo=False
        )

        print(response)

        response_text = response["choices"][0]["text"] + '```' 

        action, action_input = self.extract_action_from_response(response_text)

        if action == "get_weather":
            return get_weather(action_input["location"])
        else:
            return response["choices"][0]["text"].strip()


    