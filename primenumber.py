num = int(input("Enter a number:"))

flag = False


if num == 0 and num == 1:
    print("Entered number is not prime")
elif num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            flag = True
        break
    if flag:
        print("Entered number is not prime")
    else:
        print("Entered Number is prime")