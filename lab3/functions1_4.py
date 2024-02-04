def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(nums):
    result = []
    for c in nums:
        if is_prime(c):
            result.append(c)
    return result

numbers = [int(x) for x in input().split()]

print(filter_prime(numbers))