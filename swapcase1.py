name = "PrithviKumarDetne I am 37 years Old"

name_list = list(name)

print(name_list)

name_swap_list = []

for i in name_list:
    if i.isupper():
        i = i.lower()
        name_swap_list.append(i)
    elif i.islower():
        i = i.upper()
        name_swap_list.append(i)
    else:
        name_swap_list.append(i)
print(name_swap_list)

name_new_string = ''

for j in name_swap_list:
    name_new_string += j
print(name_new_string)
