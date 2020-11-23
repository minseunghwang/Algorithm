import collections

example = ['a','b','c','d','a','a','b']

print(collections.Counter(example))


ms  = collections.defaultdict(int)

for i in range(len(example)):
    ms[i] = example[i]


print(ms.keys())
print(ms.values())
print(ms.items())