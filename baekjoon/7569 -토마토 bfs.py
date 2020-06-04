





m,n,h = list(map(int,input().split()))
print(m,n,h)

matrix = [[[0]*m for i in range(n)] for j in range(h)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            matrix[h][n][m] = 0

print(matrix)
