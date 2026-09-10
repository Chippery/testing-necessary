from openai import OpenAI
from pathlib import Path
import json

with open("key.json", "r") as file:
    data = json.load(file)

client = OpenAI(
    base_url="https://api.aionlabs.ai/v1",
    api_key=data["key"])


folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
folder = Path(folder_path)

#for file in folder.iterdir():
#    print(file)

    
response = client.chat.completions.create(
    model="aion-labs/aion-2.0",
    messages=[{"role": "user", "content": f""}],
    temperature=0.7 # Using Aion, need to pass temperature variable
)
print(response.choices[0].message.content)
