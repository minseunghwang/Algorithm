f = open('data/1224.txt','r',encoding='UTF-8').readlines()

print(f[1])
arr1 = []
arr2= []
temp = []
answer = ''

def cal(a):
    re = ''
    for j in a:
        if j >= '0' and j <= '9':
            re += j
        if j == '*'




for cnt, i in enumerate(f[1]):
    if i == '(':
        arr1.append(cnt)
    elif i == ')':
        arr2.append(cnt)
        answer += cal(temp)
    else:
        temp.append(i)

