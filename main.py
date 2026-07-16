import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

google_api_key = os.getenv('GOOGLE_API_KEY')
MODEL = 'gemini-2.5-flash'

openai = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=google_api_key
)

# MODEL = 'llama3.2'

# openai = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="ollama"
# )

print(f"Using model: {MODEL}")

system_prompt = """
You are an expert technical tutor.
Your job is to explain technical concepts clearly and precisely.
For every answer include:

#Overview
A beginner-friendly explanation.

#How it Works
Explain the concept step by step.

#Example
Provide an example, preferably in python when applicable.

#Common Mistakes
Mention common mistakes and misconceptions that might occur.

#Summary
Finish with 3-5 bullet points summarizing the concepts.

Respond in Markdown.
"""

def get_user_question(question):
    return f"""
Please explain the following question:

{question}

Assume I have beginner to intermediate knowledge.
Use simple language whenever necessary.
"""

def answer_user_question(question):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system", "content": system_prompt},
            {"role": "user", "content":get_user_question(question)}
        ]
    )

    result=response.choices[0].message.content
    print("\n"+result+"\n")

def technical_chatbot():

    print("Technical chatbot assistant")
    print("Type 'exit' to end conversation.\n")

    while True:
        question = input("What's on your mind?  ")

        if question.lower() == "exit":
            print("See you later!")
            break

        answer_user_question(question)

        print("\n" + "-"*60 + "\n")

technical_chatbot()
