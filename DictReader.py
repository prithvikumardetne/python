import csv

with open('people.csv','r')as file:
    reader = csv.DictReader(file,delimiter='\t')
    for row in reader:
        print(dict(row))