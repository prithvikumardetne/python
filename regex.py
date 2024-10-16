import re   

pattern = r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'

test_string = '5122-4512-8965-3256'

result = re.match(pattern, test_string)

if result:
    print("Search was successful")
else:
    print("Search was unsuccessful")