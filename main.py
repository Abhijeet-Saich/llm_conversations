import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # to load the env variables

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

# response = client.chat.completions.create(
#     model = os.getenv("MODEL_1"),
#     messages = [
#         {
#             "role" : "system",
#             "content" : "you are a ruffian" 
#         },
#         {
#             "role" : "user",
#             "content" : "hello, how it's going ?" 
#         },
#     ]
# )

# print(response)
# print('------------')
# print(response.model_dump())
# print('------------')
# print(response.choices[0].message.content)




#---------------------------------------------------------------------------------------------------
# experiments showing that LLM's dont have any memory
# IMP : "Models do not remember conversations. Applications remember conversations."

response1 = client.chat.completions.create(
    model=os.getenv("MODEL_1"),
    messages=[
        {
            "role": "user",
            "content": "My name is Abhijeet"
        }
    ]
)

print(response1.choices[0].message.content)


response2 = client.chat.completions.create(
    model=os.getenv("MODEL_1"),
    messages=[
        {
            "role": "user",
            "content": "What is my name?"
        }
    ]
)

print(response2.choices[0].message.content)