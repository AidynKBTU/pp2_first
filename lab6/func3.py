word = input()
word = word.lower()
inverse = ''.join(reversed(word))
if word == inverse:
    print("Yes")
else:
    print("No")    