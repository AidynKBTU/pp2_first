import re

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    pattern = r"a[a-zA-Z1-9 ]+b"
    result = re.finditer(pattern, text)
    for index, word in enumerate(result):
        print(f'{index}:\n{word.group()}')