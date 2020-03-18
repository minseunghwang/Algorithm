import sys

# sys.stdin = open('data/1244.txt','r')
#
# for i in sys.stdin:
#     print(i)

def change(a,b):
    temp = a
    a = b
    b = temp

num,n = input().split()
n = int(n)
num = list(num)
cnt = 0
while n:
    print(num)
    num2 = list(reversed(num))
    m2 = max(num2)
    print(num.count(m2))
    ch = len(num)-num2.index(max(num2))-1
    temp = num[cnt]
    num[cnt] = num[ch]
    num[ch] = temp

    print(num)
    cnt += 1
    n -= 1





