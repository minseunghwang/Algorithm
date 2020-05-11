def sockMerchant(n, ar):
    answer = 0
    for i in set(ar):
        cnt = ar.count(i)
        answer += cnt // 2

    return answer

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n,ar))

