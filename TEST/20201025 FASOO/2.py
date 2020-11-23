from collections import defaultdict
def solution(nums):
    l = len(nums)
    answer = [0 for i in range(l)]
    q = []
    check = [0 for i in range(l)]

    for i in range(l):
        for j in range(len(nums[i])):
            if nums[i][j] not in ['0','1','2','3','4','5','6','7','8','9','-']:
                check[i] = -1
                continue
            elif  nums[i][0] == '-' or  nums[i][-1] == '-' or (j != 0 and  nums[i][j] == '-' and  nums[i][j-1] ==  nums[i][j]):
                check[i] = -1
                continue
        if check[i] != -1:
            n_cnt = nums[i].count('-')
            c_cnt = len(nums[i]) - n_cnt
            if n_cnt > 3:
                check[i] = -1
                continue
            elif c_cnt < 11 or c_cnt > 14:
                check[i] = -1
                continue
            if check[i] != -1:
                index = -1
                imsi = []
                while True:
                    index = nums[i].find('-', index+1)
                    if index == -1:
                        break
                    imsi.append(index)
                if len(imsi) == 0:
                    imsi.append(len(nums[i]))
                if imsi not in q:
                    q.append(imsi)
                answer[q.index(imsi)] += 1
    print("q", q)
    print(check)
    a = sorted(answer, reverse=True)
    a =a[:a.index(0)]

    return a

nums = ["1-2-3-12312312-3","1-2-3-456789012","582845-385823","48572-39485-89012","4-5-2-593328484","4958-39-2945123-","49582039415423","7-3-7-000000000","485723-693812","39482746582734","1-1-1-111111111","A4944-5095-4951","4851293412223", "11111111111111111111111111111","123-445-123-3211","111213231311A-2"]
print(solution(nums))