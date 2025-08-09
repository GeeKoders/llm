from anthropic import Anthropic
from dotenv import load_dotenv
import os

class prompt:
    def __init__(self, model = "claude-3-5-sonnet-20241022"):
        self.model = model
        load_dotenv()
        Anthropic_API_Key = os.getenv("Anthropic_API_Key")
        if not Anthropic_API_Key:
            raise ValueError("Anthropic_API_Key is not set in the environment variables.")
        self.client = Anthropic(api_key=Anthropic_API_Key)

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system = None):
    # print("Messages:", messages)
    if not messages:
        raise ValueError("Messages list cannot be empty")
    params = {
        "model": self.model,
        "max_tokens": 1000,
        "messages": messages
    }

    if system:
        params["system"] = system

    response = self.client.messages.create(**params)
    return response.content[0].text
