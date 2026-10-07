n = int(input("Enter number of n terms: "))

if n < 0:
    print("Fibonacci series up to", n, "is not defined.")
elif n == 0:
    print("No terms in the Fibonacci series.")
elif n == 1:
    print("The first 1 number in the Fibonacci series:")
    print(0)
else:
    first = 0
    second = 1

    print("The first", n, "numbers in the Fibonacci series:")
    print(first, end=", ")

    for i in range(1, n):
        print(second, end="")
        
        if i < n - 1:
            print(", ", end="")

        first, second = second, first + second

    print()
