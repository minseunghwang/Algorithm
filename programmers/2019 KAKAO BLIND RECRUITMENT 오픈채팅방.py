
def solution(record):
    answer = []
    dict = {}

    for i in record:
        m = i.split()
        if m[0] == 'Change':
            dict[m[1]] = m[2]
        elif m[0] == 'Leave':
            answer.append([m[1],0])
        elif m[0] == 'Enter':
            dict[m[1]] = m[2]
            answer.append([m[1],1])

    temp = []
    for i in answer:
        if i[1] == 1:
            temp.append(dict[i[0]] + '님이 들어왔습니다.')
        else:
            temp.append(dict[i[0]] + '님이 나갔습니다.')

    return temp

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))