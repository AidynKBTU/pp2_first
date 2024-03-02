import os

def check_access(path):
    access_info = {
        "existence": os.path.exists(path),
        "readability": os.access(path, os.R_OK),
        "writability": os.access(path, os.W_OK),
        "executability": os.access(path, os.X_OK)
    }
    return access_info

myF = input()

access_result = check_access(myF)

print(f"Path: {myF}")
print(f"Exists: {access_result['existence']}")
print(f"Readable: {access_result['readability']}")
print(f"Writable: {access_result['writability']}")
print(f"Executable: {access_result['executability']}")
