def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None, None

numheads = 35
numlegs = 94
result_chickens, result_rabbits = solve(numheads, numlegs)

if result_chickens is not None:
    print(f"Number of chickens: {result_chickens}")
    print(f"Number of rabbits: {result_rabbits}")
else:
    print("No solution found.")
