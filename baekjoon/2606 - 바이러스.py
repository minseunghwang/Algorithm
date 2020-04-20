

computer = int(input())
ssang = int(input())
p = []
matrix = [[0]*(computer+1) for _ in range(computer+1)]

for i in range(ssang):
     a,b= list(map(int,input().split()))
     matrix[a][b] = 1
     matrix[b][a] = 1

for cnt, i in enumerate(matrix[1]):
    if i == 1:
        p.append(cnt)

virus = [0] * (computer+1)
virus[1] = 1
while p:
    q = p.pop(0)
    virus[q] = 1
    for cnt, i in enumerate(matrix[q]):
        if i == 1 and virus[cnt] != 1:
            p.append(cnt)

print('virus:', sum(virus)-1)
print(virus)
print(matrix)





