from collections import Counter


def solution(s, n):
    count = Counter(s).values()
    print(count)

    while n:

        n -= 1

    # a,b = count.most_common(n=1)[0]
    # print(count)
    # print(count.values())


    return 0

s = "aaaaabbc"
n=1
print(solution(s,n))