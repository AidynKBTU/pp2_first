def unique(nums):
    result = []
    for c in nums:
        if c not in result:
            result.append(c)
    print(*result)

numbers = [int(x) for x in input().split()]

unique(numbers)