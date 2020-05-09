def solution(board, moves):
    answer = 0

    stack = []

    while moves:
        now = moves.pop(0)-1
        for i in board:
            if i[now] != 0:
                stack.append(i[now])
                i[now] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))

