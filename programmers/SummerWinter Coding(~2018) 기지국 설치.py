def solution(n, stations, w):
    answer = 3

    visit = [0] * (n+1)

    for station in stations:
        for i in range(-w,w+1,1):
            if 1 <= station+i <= n:
                visit[station+i] = 1

    len = 0
    answer = 0
    print(visit[1:])
    for v in visit[1:]:
        if v == 0:
            len += 1
        elif (v == 1):
            answer += ((len-1) // ((2*w)+1))+1
            len = 0
    if len != 0:
        print('len',len)
        answer += ((len-1) // ((2*w)+1))+1

    return answer


# n = 15
# stations = [4,11]
# w = 1

n = 15
stations = [1,9]
w = 2

print(solution(n,stations,w))

