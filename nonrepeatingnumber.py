s = 'concussion'

s_list = list(s)

print(s_list)

for i in range(len(s_list)):
    for j in range(len(s_list+1)):

        if s_list[i] == s_list[i+1]:
        break
print(s_list[5])