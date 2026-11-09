import os
import argparse
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

    # Get user prompt as argument
    parser = argparse.ArgumentParser(
        prog='bootdev agent',
        description='bootdev ai chatbot tool'
    )
    parser.add_argument("user_prompt", type=str, help="type in a prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args: str = parser.parse_args()

    messages: list = [
        {"role": "user", "content": args.user_prompt},
    ]

    # Get response from model
    print("Hello from ai-agent!")
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    # Optional verbose output
    if args.verbose:
        print(f"User Prompt: {args.user_prompt}") # User input
        if response.usage is None:
            raise RuntimeError("could not get response.usage, try again")   # vv Keep track of token usage!!vv
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {completion_tokens}")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
