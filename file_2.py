import csv

with open('employee_updated.csv','r')as file:
    reader = csv.DictReader(file,delimiter='\t')
    for row in reader:
        print(dict(row))