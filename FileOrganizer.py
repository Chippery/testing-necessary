import os 
import shutil

file_Types = {
    ".jpg" : "Images",
    ".mp4" : "Videos",
    ".gif" : "Gifs",
    ".txt" : "Text",
    ".exe" : "Executable"
}

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
target_dir = r"c:\Users\chipp_hqhjylc\Downloads"
dir_list = os.listdir(target_dir)

dir_keys = list(file_Types.keys())

list_of_files = ["Code.jpg", "Ex.mp4", "Youtube.txt"]


for i in list_of_files: # Creates files in downloads path
    with open(os.path.join(create_folder_path, i), "w") as file:
        file.write("print('Hello from the dynamically created file!')\n")

try: # Attempts to create folders in downloads path
    for i in file_Types:
        create_folder_path = (fr"{create_folder_path}\{file_Types[i]}")
        os.makedirs(create_folder_path, exist_ok=False)
        create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'
except FileExistsError as e:
    print("Folder Already Exists.")

create_folder_path = r'c:\Users\chipp_hqhjylc\Downloads'

listdir = os.listdir(create_folder_path)

example_src = (create_folder_path + "\Code.jpg")
example_dst = (create_folder_path + "\Images")

for x in listdir:
    if '.jpg' in x:
        print(x)

shutil.move(example_src, example_dst) # Move src to dst