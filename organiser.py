import os
import shutil

from_dir = "C:\Users\ASUS\OneDrive\Desktop\C102_assets-main"
to_dir = "C:\Users\ASUS\OneDrive\Desktop\class102"

list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + 'C:\Users\ASUS\OneDrive\Desktop\C102_assets-main\ChatBot-01.png' + file_name
        path2 = to_dir + 'C:\Users\ASUS\OneDrive\Desktop\class102' + "image_files"
        path3 = to_dir + 'C:\Users\ASUS\OneDrive\Desktop\class102\abc' + file_name
        if os.path.exists(path2):
            print("Moving" + file_name + "")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + file_name + "")
            shutil.move(path1,path3)

        