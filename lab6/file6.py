import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"content  of {file_name}")

for _ in range(26):
    generate_text_files()