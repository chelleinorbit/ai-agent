import os
from dotenv import load_dotenv
from openai import OpenAI

# API key for openrouter
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("api key missing")

# Creates AI client, pointing to openrouter instead of openai
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
# Get response from model
# noinspection bad-argument-type
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        }
    ]
)



def main():
    print("Hello from ai-agent!")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
