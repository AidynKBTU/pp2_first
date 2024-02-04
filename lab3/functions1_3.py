def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        total_legs = 2 * chickens + 4 * rabbits
        if total_legs == numlegs:
            return chickens, rabbits
    return False

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result[0])
print(result[1])
