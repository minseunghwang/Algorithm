def countingValleys(n, s):
    answer, cnt = 0,0
    for i in s:
        if i == 'U':
            cnt += 1
            if cnt == 0:
                answer += 1
        elif i == 'D':
            cnt -= 1
    return answer

n=8
s='UDDDUDUUU'
print(countingValleys(n, s))

