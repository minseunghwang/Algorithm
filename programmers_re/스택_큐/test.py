# import collections
#
# example = ['a','b','c','d','a','a','b']
#
# print(collections.Counter(example))
#
#
# ms  = collections.defaultdict(int)
#
# for i in range(len(example)):
#     ms[i] = example[i]
#
#
# print(ms.keys())
# print(ms.values())
# print(ms.items())

priorities = [2, 1, 3, 2, 7, 2, 4]
q = [[1 + i, j] for i, j in enumerate(priorities)]
print(q)

q.sort(key=lambda x:x[1],reverse=True)
print(q)
print(max(q, key=lambda x:x[1]))
