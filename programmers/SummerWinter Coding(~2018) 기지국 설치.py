import math

def solution(n, stations, w):
    answer = 0

    dis = []
    for i in range(1,len(stations)):
        dis.append((stations[i]-w-1) - (stations[i-1]+w))

    front = stations[0]-w-1
    if front > 0:
        dis.append(front)

    back = n-(stations[-1]+w)
    if back > 0:
        dis.append(back)

    for i in dis:
        answer += math.ceil(i / (2*w+1))

    return answer


n = 11
stations = [4,11]
w = 1

# n = 15
# stations = [1,9]
# w = 2

print(solution(n,stations,w))

