def solution(board):
    answer = []
    l = len(board)

    check = [[0 for x in range(l)] for x in range(l)]
    cnt = 10
    while cnt:
        maxrix = [[0 for x in range(l)] for x in range(l)]
        flag = True
        for i in range(l):
            for j in range(l):
                if check[i][j] == 0 and maxrix[i][j] == 0:
                    maxrix[i][:l] = [-1] * l
                    for k in range(l):
                        maxrix[k][j] = -1
                    maxrix[i][j] = 1
                if flag and check[i][j] != 1:
                    check[i][j] = 1
                    flag = False
        print(maxrix)
        print('check', check)

        cnt -= 1
        answer.append(maxrix)



    return answer


board = [[3,6,8],[1,4,7],[2,1,4]]

print(solution(board))