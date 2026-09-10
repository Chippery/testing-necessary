from openai import OpenAI
from pathlib import Path
import json

with open("key.json", "r") as file:
    data = json.load(file)

client = OpenAI(
    base_url="https://api.aionlabs.ai/v1", # base_url will be your ai's url
    api_key=data["key"] # Key will be your api's key
    )

folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
folder = Path(folder_path)
    
response = client.chat.completions.create(
    model="aion-labs/aion-2.0",
    messages=[{"role": "user", "content": f""}],
    temperature=0.7 # Using Aion, need to pass temperature variable
)
print(response.choices[0].message.content)
