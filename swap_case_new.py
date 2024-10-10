swap_string = "Pythonist 2"

swap_list = list(swap_string)

print(swap_list)

swap_list_new = []

for i in swap_list:
    if i.isupper():
        i = i.lower()
        swap_list_new.append(i)
    elif i.islower():
        i = i.upper()
        swap_list_new.append(i)
    else:
        swap_list_new.append(i)
print(swap_list_new)

swap_new_string = ''
for j in swap_list_new:
    swap_new_string += j
print(swap_new_string)

