import asyncio
import openai
import os
from openai import ChatCompletion
from dotenv import load_dotenv

history = []

async def main():
    print("Type 'q' to quit.")
    while (message := input("> ")) != "q":
        print(await get_response(message), end="\n\n")


async def get_response(content):
    history.append({"role": "user", "content": content})
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    resp = await ChatCompletion.acreate(model="gpt-3.5-turbo",messages=history)
    output = resp["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": output})
    return output


if __name__ == "__main__":
    asyncio.run(main())
