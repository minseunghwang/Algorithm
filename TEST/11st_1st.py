S = 'tegsornamwaresomran'
S = 'wreawerewa'
S = 'aaaaaa'
pattern = 'ransom'
pattern = 'ware'
pattern = 'a'


def solution(S,pattern):
    l = len(pattern)
    dict = {}
    for i in pattern:
        dict[i] = pattern.count(i)

    cnt = 0
    for i in range(len(S)-l+1):
        dict2 = {}
        for j in S[i:i+l]:
            temp = S[i:i+l]
            dict2[j] = temp.count(j)
        if dict == dict2:
            cnt += 1
    return cnt

print(solution(S,pattern))