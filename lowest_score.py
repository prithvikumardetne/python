students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

student_set = tuple(students)

print(student_set)

# Create a dictionary to hold the nested lists
students_by_score = {score: name for name,score in student_set}

print(type(students_by_score))

print(students_by_score)

sorted_by_keys = dict(sorted(students_by_score.items()))

sorted_list = list(sorted_by_keys.values())

sorted_list_updated = sorted_list[:2]

for names in sorted_list_updated:
    print(names)