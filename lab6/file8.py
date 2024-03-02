import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print("File deleted")
            except Exception as e:
                print("error")
    else:
        print("File not exist.")

file_path = input()

delete_file(file_path)
