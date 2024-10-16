str = 'HackerRank.com presents "Pythonist 2".'

str_list = list(str)

#print(str_list)

str_list_updated = []

for s in str_list:
    if s.islower():
        s = s.upper()
        str_list_updated.append(s)
    elif s.isupper():
        s = s.lower()
        str_list_updated.append(s)
    else:
        str_list_updated.append(s)
#print(str_list_updated)

after_swap_string =''
for elements in str_list_updated:
    after_swap_string += elements
print(after_swap_string)
