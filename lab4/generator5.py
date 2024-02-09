def numbers(n):
    while n >=0:
        yield n
        n -= 1
        
n = 8
print(f"Numbers from {n} to 0:")
for x in numbers(n):
    print(x)