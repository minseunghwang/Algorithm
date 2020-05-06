from collections import deque

def solution(n, road, k):
    answer = 0

    matrix = [[0]*(n+1) for _ in range(n+1)]

    for a,b,c in road:
        if matrix[a][b] == 0 and matrix[b][a] == 0:
            matrix[a][b] = c
            matrix[b][a] = c
        else:
            if matrix[a][b] > c:
                matrix[a][b] = c
                matrix[b][a] = c

    q = deque()
    q.append(1)

    dis = [10000]*(n+1) # 1부터 각 지점까지 걸리는 거리
    dis[1] = 0

    print(matrix[1:])
    print(dis[1:])

    while q:

        p = q.popleft()
        for i in range(1,len(matrix)):
            if matrix[p][i] != 0:
                if dis[i] > dis[p] + matrix[p][i] and dis[p] + matrix[p][i] <= k:
                    dis[i] = dis[p] + matrix[p][i]
                    q.append(i)
    print(len([i for i in dis if i <= k]))

    return answer

#
# n = 5
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# k =3
n = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
k = 4
#
print(solution(n,road,k))

# import math
# distance = [math.inf for _ in range(n+1)]
# print(distance)