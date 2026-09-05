import os 
import shutil

file_Types = {
    ".jpg" : "Images",
    ".mp4" : "Videos",
    ".gif" : "Gifs",
    ".txt" : "Text",
    ".exe" : "Executable",
    ".ini" : "Initialization",
    ".java" : "Java_File",
    ".jpeg" : "Images",
    ".png" : "Images"
}

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'

try: # Attempts to create folders in downloads path
    for i in file_Types:
        create_folder_path = (fr"{create_folder_path}\{file_Types[i]}")
        os.makedirs(create_folder_path, exist_ok=False)
        create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
except FileExistsError as e:
    print("Folder Already Exists.")

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'

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
    except shutil.Error as e:
        print("Some stupid file already exists, can't move it.") # Can't and Won't move if file already exists
