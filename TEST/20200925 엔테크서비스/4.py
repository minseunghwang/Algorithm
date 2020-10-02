def solution(t1, t2):
    answer = -1

    t2_mat = [[0]*len(t2) for i in range(len(t2))]

    for i in range(len(t2)):
        print(t2[i])
        # if t2[i][1] != -1:
        #     print(t2[i][t2[i][1]])

    return answer

t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
t2 = [[1,2],[-1,-1],[-1,-1]]
print(solution(t1,t2))