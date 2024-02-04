def histogram(nums):
    for c in nums:
        print('*'*c)

numbers = [int(x) for x in input().split()]

print(histogram(numbers))