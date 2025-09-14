# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=API_KEY)

# def call_openai(prompt, model="gpt-4o-mini"):
#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": "You are a grounded YouTube advisor. Only use provided context and cite sources."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3,
#     )
#     return response.choices[0].message.content

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment or .env file.")

# Initialize client WITHOUT 'proxies' argument
client = OpenAI(api_key=API_KEY)

def call_openai(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a grounded YouTube advisor. Only use provided context and cite sources."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

