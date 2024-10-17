str = 'chris alan'

str_updated = str.split(" ")

#print(str_updated)

str_list = []

for case in str_updated:
    str_list.append(case.capitalize())
#print(str_list)

string_after_capitalize =str_list[0] + " " + str_list[1]

print(string_after_capitalize)
