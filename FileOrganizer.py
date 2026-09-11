from openai import OpenAI
import os 
import shutil
import json
import ast

counter = 0
create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads' # Change with path you want to clean up
listdir = os.listdir(create_folder_path)
file_list = []

with open("key.json", "r") as file:
    data = json.load(file)

with open("fileRecognize.json", "r") as Fold:
    folderNames = json.load(Fold)

for i in folderNames["categories"]: # Attempts to create folders in downloads path
    folder_path_name = (fr"{create_folder_path}\{folderNames["categories"][counter]["name"]}") # Set full path to make folder
    os.makedirs(folder_path_name, exist_ok=True)
    counter += 1

for eachFile in listdir: # Add files not in directory into list to sort later
    if os.path.isfile(fr"{create_folder_path}\{eachFile}"):
        file_list.append(eachFile)


client = OpenAI(
    base_url="https://api.groq.com/openai/v1", # base_url will be your ai's url
    api_key=data["key"] # Key will be your api's key
    )
    
response = client.chat.completions.create(
    model="groq/compound-mini",
    messages=[{"role": "user", "content": 
            f"Read the files: {file_list} and return JUST a list with each index being 0-11 for each file depending on their file type based"
            f"on {[cat["name"] for cat in folderNames["categories"]]}, these files types {[ext["extensions"] for ext in folderNames["categories"]]} are" 
             "assigned to the same index as the folder indexes, use them to help you sort."}],
    temperature=0.7
)
AI_response = ast.literal_eval(response.choices[0].message.content)

for index, item in enumerate(file_list): # Indexing through files not in an folders
    try:
        shutil.move(fr"{create_folder_path}\{item}", fr"{create_folder_path}\{folderNames["categories"][AI_response[index]]["name"]}") # Move src to dst
        print(fr"Moved {item} to {create_folder_path}\{folderNames["categories"][AI_response[index]]["name"]}")
    except shutil.Error as e:
        print(fr"Some stupid file named {item} already exists inside {create_folder_path}\{folderNames["categories"][AI_response[index]]["name"]}, can't move it.") # Can't and Won't move if file already exists
print(AI_response)
