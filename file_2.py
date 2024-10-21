import csv

with open('employee_updated.csv','r')as file:
    reader = csv.reader(file,delimiter='\t')
    for row in reader:
        print(row)