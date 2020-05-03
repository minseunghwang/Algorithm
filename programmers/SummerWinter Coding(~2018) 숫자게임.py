def solution(A,B):
    answer = 0

    A.sort()
    B.sort()

    while len(A) and len(B):
        if A[0] < B[0]:
            answer += 1
            A.pop(0)
            B.pop(0)
        else:
            B.pop(0)

    return answer


A = [5,1,3,7]
A = [2,2,2,2]
# B = [2,2,6,8]
B = [1,1,1,1]
print(solution(A,B))
