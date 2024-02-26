#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    pattern = r"ab*"
    result = re.findall(pattern, text)
    print(result)