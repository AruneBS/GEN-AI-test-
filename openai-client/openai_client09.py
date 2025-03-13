import os
from openai import OpenAI

from dotenv import load_dotenv
from rich import print 

load_dotenv()


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

#response = client.chat.completions.create(
chat_completion= client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "Generate me a python code to read a file",
        }
    ],
    model="gpt-4o",
    #temperature=1,
    #max_tokens=4096,
    #top_p=1
)

print(chat_completion)
