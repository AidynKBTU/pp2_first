def reverse_sent(n):
    new = n[::-1]
    print(*new)

sentence = [str(x) for x in input().split()]

reverse_sent(sentence)