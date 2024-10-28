mylist = [2,5,6,8,10,]

new_list = list(filter(lambda x : (x%2==0) , mylist))

print(new_list)