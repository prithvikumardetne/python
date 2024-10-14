# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fset = frozenset(vowels)

print(fset)

person = {"name": "John", "age": 23, "sex": "male"}

fset = frozenset(person)

print(fset)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

C = A.copy()

print(C)

print(A.union(B))

print(A.intersection(B))

print(A.difference(B))

print(A.symmetric_difference(B))