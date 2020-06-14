from collections import defaultdict
trash = int(input())
n = list(map(int,input().split()))
trash2 = int(input())
m = list(map(int,input().split()))
d = defaultdict(int)
for i in n:
    d[i] += i
for i in m:
    if d[i]:
        print(1)
    else:
        print(0)


# for i in m:
#     if i in nn:
#         print(1)
#     else:
#         print(0)
