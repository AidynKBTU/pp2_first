import os

def list_directories(path):
    return [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]

def list_files(path):
    return [entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))]

def list_all_contents(path):
    return os.listdir(path)

my = input()

print("Directories:")
print(list_directories(my))

print("\nFiles:")
print(list_files(my))

print("\nAll Directories and Files:")
print(list_all_contents(my))
