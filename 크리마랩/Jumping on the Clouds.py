def jumpingOnClouds(c):
    idx, cnt = 0, 0
    while True:
        if idx == (len(c) -2):
            return cnt+1
        if idx == len(c) -1 :
            return cnt
        if c[idx+2] == 0:
            idx = idx + 2
        elif c[idx+1] == 0:
            idx = idx + 1
        cnt += 1



c = [0, 0, 0, 1, 0, 0]
# c = [0, 0]
# c = [0, 0, 1, 0, 0, 1, 0]
# c = [0, 1, 0, 1, 0, 0, 1, 0]
# c = [0, 1, 0, 0, 1, 0, 1, 0]

print(jumpingOnClouds(c))

# def jump(cnt, idx):
#     print(cnt, idx)
#     if idx == (len(c) - 1):
#         answer = cnt
#         return cnt
#
#     cnt += 1
#     if c[idx + 2] == 0:
#         jump(cnt, idx + 2)
#     else:
#         jump(cnt, idx + 1)
#
# def jumpingOnClouds(c):
#     a = 0
#
#
#     answer = jump(a,0)
#     print(answer)
#     return a

