from openai import OpenAI
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = """
You are ChatGPT, specialized in converting natural language Git requests into precise Git commands. Accurately interpret each user request related to Git operations and generate only the corresponding Git command(s) using placeholders like <repository_url> when needed, without any additional explanations.
"""

def generate_responses():
    with open(r'Days\009\openai_distillation\user_messages.json', 'r') as file:
        user_messages = json.load(file)

    for sentence in user_messages['requests']:
        # call the OpenAI model gpt-4o-mini
        response= client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:personal:git:AF7QSF0m",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                "role": "user",
                "content": sentence
                },
            ],
            store=True,
            metadata={
                "task":"git"
            }
        )

generate_responses()
