def solution(priorities, location):
    answer = 0
    max_ = max(priorities)
    q = [[i,j] for i,j in enumerate(priorities)]

    while q:
        print(q)
        f,e = q.pop(0)
        if e == max_:
            if f == location:
                return answer
            answer += 1
            max_ = max(q,key=lambda x:x[1])[1]

        else:
            q.append([f,e])

    return answer

# priorities = [2, 1, 3, 2]
# priorities = [1, 1, 9, 1, 1, 1]
priorities = [1, 1, 1, 1, 1, 1, 1]

# location = 2
# location = 0
location = 6


print(solution(priorities,location))