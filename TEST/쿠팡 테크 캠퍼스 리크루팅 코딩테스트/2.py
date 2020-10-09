import datetime
import copy
def solution(n, customers):
    answer = 0
    customers.sort()
    cho = datetime.datetime.strptime('01/01 00:00:01','%m/%d %H:%M:%S')
    q = [cho for i in range(n)]
    qcnt = [0 for i in range(n)]
    print(customers)
    for i in range(len(customers)):
        flag = 0
        a = datetime.datetime.strptime(customers[i][:-3],'%m/%d %H:%M:%S')
        b = datetime.datetime.strptime(customers[i][-2:],'%M').minute
        # print(a + datetime.timedelta(minutes=b))
        for j in range(len(q)):
            if q[j] < a:
                print('j',j,q[j],a)
                q[j] = a + datetime.timedelta(minutes=b)
                qcnt[j] += 1
                flag = 1
                break
        if flag == 0:
            print('he')
            q[q.index(min(q))] = a + datetime.timedelta(minutes=b)
            qcnt[q.index(min(q))] += 1
        print('q',q)
    print(qcnt)


    return answer

n = 3
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
print(solution(n,customers))


