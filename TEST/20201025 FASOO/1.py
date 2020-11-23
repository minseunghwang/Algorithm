def solution(s,idx):
    answer = []
    q1= []
    q2 = []
    d ={}

    for index, i in enumerate(s):
        if s[index] == '{' or s[index] == '}':
            if len(q2) != 0 and s[index] != q2[-1]:
                imsi = q1.pop(-1)
                d[imsi] = index
                d[index] = imsi
            else:
                q1.append(index)
                q2.append(s[index])

    print(q1)
    print(d)
    for i in idx:
        answer.append(d[i])
    return answer


s = "{cpp{java}}{python}"
idx = [0, 4, 9, 10, 11, 18]
print(solution(s,idx))