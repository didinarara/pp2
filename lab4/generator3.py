def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i
def main():
    num = int(input("Enter a number:"))
    divisors = divisible_by_3_and_4(num)
    
    print("Numbers divisible by 3 and 4 are:")
    for x in divisors:
        print(x)
        
if __name__ == "__main__":
    main()