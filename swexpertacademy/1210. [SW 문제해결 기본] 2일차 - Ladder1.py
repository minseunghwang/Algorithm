f = open('data/1210.txt','r',encoding='UTF8').readlines()
#
# matrix = []
# for i in f[1:101]:
#     matrix.append(i.split())
# now = matrix[99].index('2')
# visit = [[0] * 100 for _ in range(100)]

# def dfs(cnt,x):
#     cnt -= 1
#     visit[cnt][x] = 1
#     print(cnt)
#     while cnt != 0:
#         if cnt == 0:
#             return x
#         if visit[cnt][x-1] == 0 and matrix[cnt][x-1] == '1':
#             cnt += 1
#             dfs(cnt, x-1)
#         elif visit[cnt][x+1] == 0 and matrix[cnt][x+1] == '1':
#             cnt += 1
#             dfs(cnt, x+1)
#         else:
#             dfs(cnt,x)
#     return x
#
# c = 100
# ms = dfs(c,now)
# print(ms)


# y = 99
# while y != 0:
#     visit[y][now] = 1
#     if visit[y][now-1] == 0 and matrix[y][now-1] == '1':
#         now -= 1
#     elif visit[y][now+1] == 0 and matrix[y][now+1] == '1':
#         now += 1
#     else:
#         y -= 1
# print(now)


# for test_case in range(1, 2):
#     trash = input()
#     matrix = []
#     a = input().split()
#     for i in range(3):
#         matrix.append(a[i*3 : i*3 + 3])
#     now = matrix[2].index('2')
#     visit = [[0] * 100 for _ in range(100)]
#     y = 2
#     while y != 0:
#         visit[y][now] = 1
#         if now-1 >= 0 and visit[y][now-1] == 0 and matrix[y][now-1] == '1':
#             now -= 1
#         elif now+1 <= 99 and visit[y][now+1] == 0 and matrix[y][now+1] == '1':
#             now += 1
#         else:
#             y -= 1
#     print(f'#{test_case} {now}')

ms = []
for i in range(3):
    a = input().split()
    ms.append(a)
print(ms)

# matrix = [[] for _ in range(3)]
#
# for j in range(3):
#     matrix[2 - j] = input().split()
#
# print(matrix)
