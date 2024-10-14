def greet():
    print("Hello World")

greet()

def greet_updated(name):
    print("Hello", name)

greet_updated("john")

def addnumbers(num1,num2):
    sum = num1 + num2
    print("Sum of 2 numbers is: ", sum)

addnumbers(10,20)

def dif_numbers(num1,num2):
    Difference = num1 - num2
    print("Difference of 2 numbers are: ",Difference)

dif_numbers(20,10)

def find_square(num):
    result = num * num
    return result
square = find_square(3)

print(square)

def find_cube(num):
    result = num * num * num
    return result
Cube  = find_cube(num=8)

print(Cube)