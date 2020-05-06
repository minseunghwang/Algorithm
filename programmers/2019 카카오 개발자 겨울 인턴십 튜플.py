def solution(s):
    answer = []

    ss = s[2:-2].split('},{')
    sss = sorted(ss,key = lambda x:len(x))

    print(sss)
    for i in sss:
        for j in i.split(','):
            if j != ',' and (int(j) not in answer) :
                answer.append(int(j))

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# s = "{{123}}"
# s = "{{20,111},{111}}"

print(solution(s))