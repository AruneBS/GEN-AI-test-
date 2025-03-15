import os
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
from rich import print 

load_dotenv()


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

#from pydantic import BaseModel
#from openai import OpenAI





completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Sekmadienį Irena organizuoja šeimos pietus."},
    ],
    
)

event = completion.choices[0].message
print(event)
