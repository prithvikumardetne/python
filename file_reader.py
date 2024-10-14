import csv

with open('employee_updated.csv','r') as file:
    reader = csv.reader(file, delimiter='\t')

    employee_first_name =[]
    for row in reader:
        employee_first_name.append(row.strip().split(" ")[1])
    print(employee_first_name)
