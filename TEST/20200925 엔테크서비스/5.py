from itertools import permutations
from itertools import combinations
s = "031"
a = list(permutations(s,2))
b = list(combinations(s,2))
print(a)
print(b)

s = list(s)
print(s)
print(s.count('0'))