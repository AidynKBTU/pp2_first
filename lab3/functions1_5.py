from itertools import permutations

def print_permutations(s):
    permutation = permutations(s)
    for perm in permutation:
        print(''.join(perm))

string = input()
print_permutations(string)
