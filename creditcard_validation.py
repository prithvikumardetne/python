import re

credit_card = str(input("Enter Credit Card Number:"))

print(credit_card)

credit_card_list = list(credit_card)

creditcard_length = len(credit_card_list)

print(creditcard_length)

if len(credit_card_list) == 16:
    print("Entered Credit Card No is Valid")
else:
    print("Entered Credit Card No is Invalid")