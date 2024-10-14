def add_numbers(a=7 , b=8):
    sum = a + b
    return sum

print(add_numbers())

print(add_numbers(a=9))

print(add_numbers(b=10))


def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum = ",result)

find_sum(7,8,9)

find_sum(2,3)

find_sum(7,8,9,10,15,12)