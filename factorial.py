num = int(input("Enter the number: "))

factorial = 1

if num < 0:
    print("Factorial doesnt exist for negative numbers")
elif num == 0:
    print("Factorial for zero is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial is",factorial)