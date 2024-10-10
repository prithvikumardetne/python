swap_string = "Www.HackerRank.com"

swap_list = list(swap_string)

print(swap_list)

swap_new = []

for i in swap_list:
    if i.isupper():
        i = i.lower()
        swap_new.append(i) 
    elif i.islower():
        i = i.upper()
        swap_new.append(i) 
    else:
        swap_new.append(i) 

print(swap_new)

swap_string_final = ''

for j in swap_new:
    swap_string_final += j
print(swap_string_final)