def minimumBribes(q):
    answer = 0
    for i in range(len(q)):
        if abs(q[i] - (i+1)) > 2:
            print(i)
            return 'Too chaotic'
        if q[i] > i+1:
            answer += q[i] - (i+1)
    return answer

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    print(minimumBribes(q))