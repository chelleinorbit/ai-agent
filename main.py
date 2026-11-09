import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
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
    print("Hello from ai-agent!")
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
            }
        ]
    )
    # Keep track of token usage!!
    if response.usage is None:
        raise RuntimeError("could not get response.usage, try again")
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {completion_tokens}")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
