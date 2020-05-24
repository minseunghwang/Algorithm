from _collections import defaultdict
def solution(p):

    while True:
        p += 1
        print(p)
        sw = True
        d = defaultdict(int)
        for i in str(p):
            d[i] += 1
            if d[i] > 1:
                sw = False
                break
        if sw:
            return p

p = 1987
print(solution(p))