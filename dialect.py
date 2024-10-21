import csv

csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('office.csv','r') as file:
    reader = csv.reader(file,dialect='myDialect')
    for row in reader:
        print(row)