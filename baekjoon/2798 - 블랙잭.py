import itertools
n,m = list(map(int,input().split()))
index = list(map(int,input().split()))

print(index)
index.set()
print(index)    
def black(m,index):
    maxi = 0
    for i in itertools.permutations(index,3):
        if sum(i) == m:
            return sum(i)
        elif sum(i) < m:
            if sum(i) > maxi:
                maxi = sum(i)

    return maxi

print(black(m,index))
