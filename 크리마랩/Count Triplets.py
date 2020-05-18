from collections import defaultdict

def countTriplets(arr, r):
    answer = 0

    d = defaultdict(int)
    for i in arr:
        d[i] += 1


    if r != 1:
        for i,j in d.items():
            if i*r in d and i*r*r in d:
                answer += (j * d[i*r] * d[i*r*r])
    else :
        print(d[1])
        answer = (d[1] * (d[1]-1) * (d[1]-2)) // (1 * 2 * 3)

    return answer


nr = input().rstrip().split()
n = int(nr[0])
r = int(nr[1])
arr = list(map(int, input().rstrip().split()))
print(countTriplets(arr, r))
