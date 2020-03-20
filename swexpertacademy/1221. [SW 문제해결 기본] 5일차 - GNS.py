f = open('data/1221.txt','r',encoding='UTF-8').readlines()
a,b = f[1].split()
print(b)
print(f[2])
q = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dic = {}
for cnt,i in enumerate(q):
    dic[i] = cnt
ms = f[2].split()
print(dic)
ms.sort(key=lambda x:dic[x])
print(' '.join(ms))
# ms.sort()
# print(ms)

############################### 기똥차부렀따
T = int(input())
# q = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# dic = {}
# for cnt,i in enumerate(q):
#     dic[i] = cnt
# for test_case in range(1, T+1):
#     tr,ush = input().split()
#     ms = input().split()
#     ms.sort(key=lambda x:dic[x])
#     ms = " ".join(ms)
#     print(f'{tr} {ms}')
#