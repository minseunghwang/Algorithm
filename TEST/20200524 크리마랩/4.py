def droppedRequests(requestTime):
    answer = 0
    end = requestTime_count
    if requestTime_count > 20:
        end = 21
    now = 0
    first = requestTime[0]
    for i in range(end):
        if first + 59 < requestTime[i]:
            print('1')
            answer += 1
            continue
        if now != requestTime[i]:
            now = requestTime[i]
            cnt = 1
        else:
            cnt += 1
            if cnt > 3:
                print('2',i)
                answer += 1
                continue
    answer += requestTime_count - 20
    print(answer)
    return answer
'''
21
1
1
1
1
2
2
2
3
3
3
4
4
4
5
5
5
6
6
6
7
7

31 84 64

'''


if __name__ == '__main__':
    requestTime_count = int(input().strip())
    requestTime = []
    for _ in range(requestTime_count):
        requestTime_item = int(input().strip())
        requestTime.append(requestTime_item)

    result = droppedRequests(requestTime)
