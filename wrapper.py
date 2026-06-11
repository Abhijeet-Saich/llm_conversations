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



class Agent:
    def __init__(self, name, system_prompt, model):
        self.name = name,
        self.model = model

        self.messages = [
            {
                "role" : "system",
                "content" : system_prompt
            }
        ]

    def chat(self, user_message):
        self.messages.append({
                "role" : "user",
                "content" : user_message
        })

        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        answer = response.choices[0].message.content

        self.messages.append({
            "role": "assistant",
            "content": answer
        })

        return answer
    

teacher = Agent(
    name="Teacher",
    system_prompt="""
    You are a Python teacher.

    Ask one short Python question at a time.

    Keep questions under 20 words.
    """,
    model=os.getenv("MODEL_1")
)


student = Agent(
    name="Student",
    system_prompt="""
    You are a boorish proud tech noob.

    Answer the teacher's question.

    Keep answers under 30 words.
    """,
    model=os.getenv("MODEL_1")
)

critic = Agent(
    name="Critic",
    system_prompt="""
    You are a Python expert.

    Review the student's answer.

    Point out mistakes.

    Be concise.
    """,
    model=os.getenv("MODEL_1")
)

message = teacher.chat("Ask a question")

for _ in range(5):

    print("\nTeacher:")
    print(message)

    answer = student.chat(message)

    print("\nStudent:")
    print(answer)

    review = critic.chat(
        f"""
        Question:
        {message}

        Student Answer:
        {answer}
        """
    )

    print("\nCritic:")
    print(review)

    message = teacher.chat(
        f"""
        Student Answer:
        {answer}

        Critic Review:
        {review}

        Continue teaching.
        """
    )
