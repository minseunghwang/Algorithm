def rotation(key):
    n = len(key)
    roc_key = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            roc_key[j][n-i-1] = key[i][j]
    return roc_key


def check(x,y,key,lock,expendsize,start,end):
    expendList = [[0] * expendsize for _ in range(expendsize)]

    for i in range(len(key)):
        for j in range(len(key)):
            expendList[x+i][y+j] = key[i][j]

    for i in range(start,end):
        for j in range(start,end):
            expendList[i][j] += lock[i-start][j-start]
            if expendList[i][j] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key) - 1    # 2
    end = start + len(lock)  # 5
    expendsize = len(lock) + (2*start) # 7

    for _ in range(0,4):
        for i in range(end):
            for j in range(end):
                if check(i,j,key,lock,expendsize,start,end):
                    return True
        key = rotation(key)

    return False




key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))
