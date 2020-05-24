def solution(total_sp, skills):
    ll = [0] * (len(skills)+2)
    for i in range(len(skills)-1,-1,-1):
        if ll[skills[i][1]] == 0:
            ll[skills[i][1]] = 1
        ll[skills[i][0]] += ll[skills[i][1]]
    new = []

    for i in range(len(ll)):
        new.append(ll[i]*(total_sp//sum(ll)))
    return new[1:]

total_sp = 121
skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
print(solution(total_sp, skills))