from itertools import chain


def solution(n):
    answer = []

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    x, y = 0, -1
    cnt = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1;
                x -= 1
            matrix[y][x] = cnt
            cnt += 1

    answer = [i for i in chain(*matrix) if i != 0]

    return answer