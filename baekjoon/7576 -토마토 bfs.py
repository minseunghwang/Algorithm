
from collections import deque



dx = [0,0,1,-1]
dy = [-1,1,0,0]
m,n = list(map(int,input().split()))
matrix = []
answer = 0
q = deque()
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 1:
            q.append([i,j])
    matrix.append(row)

def bfs(m,n,matrix):
    answer = 0
    while q:
        answer += 1
        for z in range(len(q)):
            a,b = q.popleft()
            for i in range(4):
                x = dx[i] + a
                y = dy[i] + b
                if (0 <= x < n) and (0 <= y < m) and matrix[x][y] == 0 :
                    q.append([x,y])
                    matrix[x][y] = 1
    for i in matrix:
        if 0 in i:
            return -1

    return answer-1

print(bfs(m,n,matrix))
#

