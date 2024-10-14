# Frozensets
# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

print(A.isdisjoint(C))

print(C.issubset(B))

print(B.issuperset(C))