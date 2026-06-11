import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


#wrapper function to create an agent
def chat(msgs, model):
    response = client.chat.completions.create(
        model = model,
        messages = msgs
    )

    return response.choices[0].message.content

