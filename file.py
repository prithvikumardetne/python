import csv 

list_row= []

with open('employee.csv','r') as file:
    reader = csv.reader(file)
        
    for row in reader:
        print(row)
list_id = []
 
for id in reader:
    list_id.append(id[0])
print(list_id)
    
