from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
Anthropic_API_Key = os.getenv("Anthropic_API_Key")
if not Anthropic_API_Key:
    raise ValueError("Anthropic_API_Key is not set in the environment variables.")
client = Anthropic(api_key=Anthropic_API_Key)

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system = None, model="claude-3-5-sonnet-20241022", temperature=0.0, stream=False, stop_sequences=None):
    if not messages:
        raise ValueError("Messages list cannot be empty")
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    if system:
        params["system"] = system
    if stream:
        params["stream"] = True

        with client.messages.stream(**params) as stream:
            for chunk in stream:
                if hasattr(chunk, "choices"):
                    return chunk.choices[0].message

    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    response = client.messages.create(**params)
    return response.content[0].text