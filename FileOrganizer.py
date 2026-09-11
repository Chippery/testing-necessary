from openai import OpenAI
from pathlib import Path
import os 
import shutil
import json
import ast

counter = 0
create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads' # Change with path you want to clean up

with open("key.json", "r") as file:
    data = json.load(file)
    
with open("fileRecognize.json", "r") as Fold:
    folderNames = json.load(Fold)

for i in folderNames["categories"]: # Attempts to create folders in downloads path
    folder_path_name = (fr"{create_folder_path}\{folderNames["categories"][counter]["name"]}") # Set full path to make folder
    os.makedirs(folder_path_name, exist_ok=True)
    counter += 1

listdir = os.listdir(create_folder_path)
file_list = []

example_src = (fr"{create_folder_path}\{eachFile}") # src = path + file name
example_dst = (fr"{create_folder_path}\{file_Types[os.path.splitext(eachFile)[1]]}") # dst = path + folder name

client = OpenAI(
    base_url="https://api.groq.com/openai/v1", # base_url will be your ai's url
    api_key=data["key"] # Key will be your api's key
    )

folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
folder = Path(folder_path)
    
response = client.chat.completions.create(
    model="groq/compound-mini",
    messages=[{"role": "user", "content": 
            f"Read the files: {file_list} and return JUST a list with each index being 0-11 for each file depending on their file type based"
            f"on {[cat["name"] for cat in folderNames["categories"]]}, these files types {[ext["extensions"] for ext in folderNames["categories"]]} are" 
             "assigned to the same index as the folder indexes, use them to help you sort."}],
    temperature=0.7
)
AI_response = ast.literal_eval(response.choices[0].message.content)
print(AI_response)

try:
    shutil.move(example_src, example_dst) # Move src to dst
    print(f"Moved {eachFile} to {file_Types[os.path.splitext(eachFile)[1]]}")
except shutil.Error as e:
    if eachFile in os.listdir(example_dst): # Checks if file is in directory folder
        os.remove(example_src)
        print(f"Removed {eachFile}, duplicate")
    else:
        print(fr"Some stupid file named {eachFile} already exists inside {file_Types[os.path.splitext(eachFile)[1]]}, can't move it.") # Can't and Won't move if file already exists
