import re

pattern = r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'
pattern = r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'


test_string = '5748-5896-5521-4563'

result = re.match(pattern, test_string)

if result:
    print("Credit Card is Valid")
else:
    print("Credit Card No is invalid")