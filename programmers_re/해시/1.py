import collections

def solution(participant, completion):
    d = collections.defaultdict(int)

    for i,j in zip(participant,completion):
        print(i,j)

    for j in completion:
        d[j] -= 1
    print(d)
    print(d.keys())
    for i in d.keys():
        if d[i] == 1:
            return i

    # return d




# participant = ["leo", "kiki", "eden"]
participant =["mislav", "stanko", "mislav", "ana"]
# completion = ["eden", "kiki"]
completion = ['stanko', 'ana', 'mislav']
print(solution(participant,completion))