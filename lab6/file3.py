import os

def analyze_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return directory, filename
    else:
        return None, None

my = input()

directory, filename = analyze_path(my)

if directory and filename:
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print("Path does not exist.")
