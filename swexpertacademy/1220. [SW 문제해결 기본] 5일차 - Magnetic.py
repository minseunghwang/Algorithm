# 최종코드
for test_case in range(1, 11):
    matrix = []
    for i in range(int(input())):
        matrix.append(input().split())

    answer = 0
    for i in range(100):
        checklist = []
        for j in range(100):
            if matrix[j][i] != '0':
                checklist.append(matrix[j][i])
        answer += ''.join(checklist).count('12')

    print(f'#{test_case} {answer}')


# 푸느라 낑낑댄거

# a = open('data/1220.txt', 'r', encoding='UTF-8').readlines()
#
#
# print(a[1].split())
#
#
# matrix = []
# for i in range(1,101):
#     matrix.append(a[i].split())
# print(matrix)
#
# answer = 0
# for i in range(100):
#     checklist = []
#     for j in range(100):
#         if matrix[j][i] != '0':
#             checklist.append(matrix[j][i])
#     answer += ''.join(checklist).count('12')
