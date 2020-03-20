# f = open('data/1230.txt','r',encoding='UTF-8').readlines()
# a = f[1].split()
# b = f[3].split()
# b.append('END')
# print(b)
# temp = []
# for i in b:
#     temp.append(i)
#     if len(temp) > 1:
#         if temp[-1] >= 'A':
#             if temp[0] == 'I':
#                 for _ in range(int(temp[2])):
#                     a.insert(int(temp[1]),temp.pop(-2))
#
#             elif temp[0] == 'D':
#                 for _ in range(int(temp[2])):
#                     a.pop(int(temp[1]))
#
#             elif temp[0] == 'A':
#                 for _ in range(int(temp[1])):
#                     a.append(temp.pop(0))
#             temp=[i]
# print(a[:10])
#
#
#

################# answer

for test_case in range(1, 11):
    TR = input()
    a = input().split()
    ASH = input()
    b = input().split()
    b.append('END')

    temp = []
    for i in b:
        temp.append(i)
        if len(temp) > 1 and temp[-1] >= 'A':
            if temp[0] == 'I':
                for _ in range(int(temp[2])):
                    a.insert(int(temp[1]), temp.pop(-2))

            elif temp[0] == 'D':
                for _ in range(int(temp[2])):
                    a.pop(int(temp[1]))

            elif temp[0] == 'A':
                for _ in range(int(temp[1])):
                    a.append(temp.pop(0))
            temp = [i]
    answer = ' '.join(a[:10])
    print(f'#{test_case} {answer}')