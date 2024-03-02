text = input()
big = sum(1 for c in text if c.isupper())
small = sum(1 for c in text if c.islower())
print(big, small)