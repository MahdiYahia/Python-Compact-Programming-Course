number = int(input("Enter a non-negative number: "))

if number < 0:
    print("Negative number entered.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i

    print("The factorial of", number, "is:", factorial)
