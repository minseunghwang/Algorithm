

def calc(k,cal,idx):
    global maxv, minv
    print(k,cal,maxv, minv)
    if idx == n:
        maxv = max(k,maxv)
        minv = min(k,minv)
        return

    if cal[0] > 0:
        calc(k+number[idx], [cal[0]-1, cal[1], cal[2], cal[3]], idx+1)
    if cal[1] > 0:
        calc(k-number[idx], [cal[0], cal[1]-1, cal[2], cal[3]], idx+1)
    if cal[2] > 0:
        calc(k*number[idx], [cal[0], cal[1], cal[2]-1, cal[3]], idx+1)
    if cal[3] > 0:
        calc(int(k/number[idx]), [cal[0], cal[1], cal[2], cal[3]-1], idx+1)


minv = 1e9
maxv = -1e9+1
n = int(input())
number = list(map(int,input().split()))
cal = list(map(int,input().split()))
idx = 1

calc(number[0],cal,idx)
print(maxv, minv)

