
def solution(dirs):
    start = [5,5]
    visit = []
    for i in dirs:
        temp = start.copy()
        if i == 'U':
            if 0 <= start[1]-1 :
                temp[1] = start[1] - 1

        elif i == 'R':
            if start[0]+1 <=10:
                temp[0] = start[0] + 1

        elif i == 'D':
            if start[1]+1 <= 10:
                temp[1] = start[1] + 1

        elif i == 'L':
            if start[0] -1 >= 0:
                temp[0] = start[0] - 1

        if start != temp:
            visit.append([start,temp])
            start = temp.copy()
    print(visit)

    nvisit = []
    for i in visit:
        tmp = sorted(i)
        if tmp not in nvisit:
            nvisit.append(tmp)

    return len(nvisit)


dirs = 'ULURRDLLU'
dirs = 'LULLLLLLU'
# dirs = 'LRUDLURD'
# dirs = 'RRRRRDDDDDD'
dirs = 'RRRRRRRRRRUUUUUU'

print(solution(dirs))