list = [10,20,30,40,10,20,50,'hello']

empty_list = []

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list(i)==list(j) and list(i) not in empty_list:
            empty_list.append
print(empty_list)