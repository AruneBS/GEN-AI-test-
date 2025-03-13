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



class CalendarEvent(BaseModel):
   event_name: str
   date: str
   participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Sekmadienį Irena organizuoja šeimos pietus."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed 
print(event)
