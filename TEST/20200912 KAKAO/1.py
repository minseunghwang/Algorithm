def solution(new_id):
    answer = new_id.lower()

    for i in range(len(answer)):
        if not answer[i].isalpha() and not answer[i].isnumeric() and answer[i] != '-' and answer[i] != '_' and answer[i] != '.':
            answer = answer.replace(answer[i],' ')
    answer = answer.replace(' ','')
    flag = False
    for i in range(len(answer)-2, -1, -1):
        if i != 0 and flag and answer[i] == '.':
            continue
        elif flag and answer[i] != '.':
            answer = answer.replace(answer[i+1:temp+2], '.')
            flag = False
            temp = 0
        if flag == False and answer[i] == '.' and answer[i+1] == '.':
            flag = True
            temp = i
        if flag and i == 0:
            answer = answer.replace(answer[i:temp + 2], '.')

    print(answer)
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]

    if len(answer) == 0:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            cnt = 0
            for i in answer[::-1]:
                if i == '.':
                    cnt += 1
                else:
                    break
            answer = answer[:-cnt]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    print(answer)

    return answer

new_id = '...!@BaT#*....y.abcdefghijklm.'
new_id = "abcdefghijklmn....p"
solution(new_id)