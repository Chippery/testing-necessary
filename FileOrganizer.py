import os 
import shutil

file_Types = { # Values will be made into folders
    ".jpg" : "Images",
    ".mp4" : "Videos",
    ".gif" : "Gifs",
    ".txt" : "Text",
    ".exe" : "Executable",
    ".ini" : "Initialization",
    ".java" : "Java_File",
    ".jpeg" : "Images",
    ".png" : "Images",
    ".zip" : "Zips",
    ".msi" : "Executable"
}

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads' # Change with path you want to clean up

# Attempts to create folders in downloads path
for i in file_Types:
    create_folder_path = (fr"{create_folder_path}\{file_Types[i]}")
    os.makedirs(create_folder_path, exist_ok=True)
    create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads' # Path you want to clean up

listdir = os.listdir(create_folder_path)
file_list = []

for dir in listdir:
    if os.path.isfile(fr"{create_folder_path}\{dir}") and dir not in file_Types.values():
        file_list.append(dir)
print(file_list)

example_dst = (create_folder_path + r"\Images")

for eachFile in file_list: # Iterate through example files to sort
    example_src = (fr"{create_folder_path}\{eachFile}") # src = path + file name
    example_dst = (fr"{create_folder_path}\{file_Types[os.path.splitext(eachFile)[1]]}")

    try:
        shutil.move(example_src, example_dst) # Move src to dst
        print(f"Moved {eachFile} to {file_Types[os.path.splitext(eachFile)[1]]}")
    except shutil.Error as e:
        print("Some stupid file already exists, can't move it.") # Can't and Won't move if file already exists
