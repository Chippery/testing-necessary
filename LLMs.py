from openai import OpenAI
from pathlib import Path
import json
import os
import ast

with open("key.json", "r") as file:
    data = json.load(file)

with open("fileRecognize.json", "r") as Fold:
    folderNames = json.load(Fold)

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
listdir = os.listdir(create_folder_path)
file_list = []

for eachFile in listdir: # Add files not in directory into list to sort later
    if os.path.isfile(fr"{create_folder_path}\{eachFile}"):
        file_list.append(eachFile)
print(file_list)

listNum = [0, 3, 4, 1, 5]

for index, item in enumerate(file_list):
    print(listNum[index], item, folderNames["categories"][listNum[index]]["name"])

# client = OpenAI(
#     base_url="https://api.groq.com/openai/v1", # base_url will be your ai's url
#     api_key=data["key"] # Key will be your api's key
#     )
    
# response = client.chat.completions.create(
#     model="groq/compound-mini",
#     messages=[{"role": "user", "content": 
#             f"Read the files: {file_list} and return JUST a list with each index being 0-11 for each file depending on their file type based"
#             f"on {[cat["name"] for cat in folderNames["categories"]]}, these files types {[ext["extensions"] for ext in folderNames["categories"]]} are" 
#              "assigned to the same index as the folder indexes, use them to help you sort."}],
#     temperature=0.7
# )
# AI_response = ast.literal_eval(response.choices[0].message.content)
# print(AI_response)
