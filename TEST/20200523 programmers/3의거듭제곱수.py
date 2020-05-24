from itertools import combinations
def solution(n):
    answer = 0

    l = [3**i for i in range(0,n)]
    print(l)

    temp = [0,1,3]
    for i in range(2,len(l)//2):
        print(temp)
        t = []
        for j in range(len(temp)):
            t.append(temp[j] + temp[-1]**2)
        temp += t
        temp.append(sum(temp))
    print(temp)

    return answer

n = 4
n = 9
print(solution(n))

# 1 3 4
# 1 3 4 10 12 13
# 28 30 37 47 49 50
