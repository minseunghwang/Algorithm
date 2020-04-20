import sys

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(m,n):
    cnt = 1
    p = [[m,n, board[0][0]]]
    while p:
        a,b,route = p.pop(0)
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if (0 <= x < r) and (0 <= y < c) and (board[x][y] not in route):
                p.append([x,y,route+board[x][y]])
                answer = max(cnt, len(route)+1)

    return answer

r,c=list(map(int,sys.stdin.readline().split()))
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

answer = 1
print(bfs(0,0))
