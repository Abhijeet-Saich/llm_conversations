import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages_cache = [
    {
        "role": "system",
        "content": "You are a cunning trickster of medieval era"
    }
]


while True:

    user_input = input("Enter your message : ")

    if(user_input.lower() == "exit"): break

    messages_cache.append({"role" : "user", "content" : user_input})

    reply = client.chat.completions.create(
        model=os.getenv("MODEL_1"),
        messages=messages_cache
    )
    print(reply.usage)

    bot_reply = reply.choices[0].message.content
    messages_cache.append({"role" : "assistant", "content" : bot_reply})

    print("Bot reply : ", bot_reply)
