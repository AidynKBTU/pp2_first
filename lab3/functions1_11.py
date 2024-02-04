def is_palindrome(word):
    return word == word[::-1]

n = input()

print(is_palindrome(n))