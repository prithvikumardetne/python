import csv 

name = []

with open('employee.csv','r') as file:
    for row in file:
        name.append(row.strip().split(" ")[1])

print(name)