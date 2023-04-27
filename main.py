import openai
import os
from dotenv import load_dotenv

def main():
    print("Type 'exit' to quit.")
    while True:
        message = input("Input: ")
        if message == "exit":
            break
        print(get_response(message)["content"])


def get_response(message):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message


if __name__ == "__main__":
    main()
