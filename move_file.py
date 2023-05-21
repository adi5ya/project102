import os 
import shutil

from_dir = 'C:/Users/Hp/Documents'
to_dir = 'C:/Users/Hp/Desktop/document_files'

list_of_files =  os.listdir(from_dir)
#print(list_of_files)

folder = "Document_files"
path = os.path.join(to_dir,folder)


for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == ' ':
        continue
    if extension in ['.txt','.docx','.doc','pdf'] : 
        path1 = from_dir + '/' + file_name                               
        path2 = to_dir + '/' + "Document_Files"                           
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name 

        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)