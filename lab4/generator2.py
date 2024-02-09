def even_generator(n):
    for i in range(0, n+1, 2):
        yield i
            
def main():
    n = int(input("Enter a number:"))
    
    even_numbers = even_generator(n)
    
    print("Even numbers from 0 and", n, "are:", end=" ")
    print(*even_numbers, sep=", ")

if __name__ == "__main__" :
    main()