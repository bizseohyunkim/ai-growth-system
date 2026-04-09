import yaml
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt(prompt_file: str) -> dict:
    path = os.path.join(os.path.dirname(__file__), "..", "prompts", prompt_file)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run_agent(prompt_file: str, user_input: str) -> str:
    prompt = load_prompt(prompt_file)
    system = prompt.get("system", "You are a helpful assistant.")
    user_template = prompt.get("user_template", "{input}")
    user_message = user_template.replace("{input}", user_input)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_message},
        ],
        max_tokens=1024,
    )
    return response.choices[0].message.content
