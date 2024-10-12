my_str = "Hello this Is an Example With cased letters"

my_str_list = list(my_str.split(" "))

print(my_str_list)

words = []

for word in my_str_list:
    words.append(word.lower())
print(words)


for i in words:
    print(i)
