cookies = [1, 4, 2, 6, 5, 3]
k = 2

combinations = []
queue = []

# 첫 데이터 생성
tmp = cookies[:]  # deep copy
while tmp:
    n = tmp.pop(0)
    queue.append([[n], tmp[:]])

# DFS
while queue:
    print(queue)
    n = queue.pop()  # [1/3] 꺼내

    if n[1] == []:  # [2/3] 목표냐?
        combinations.append(n[0])
        continue

    # [3/3] 확장
    e = n[1].pop(0)  # 이번 쿠키 (남은 쿠키 중에 첫번째꺼)
    if e > n[0][-1]:  # 내가 마지막에 먹은거보다 이번 쿠키가 크냐?
        queue.append([n[0][:] + [e], n[1][:]])  # 크면 먹기
    queue.append([n[0][:], n[1][:]])  # 이번 쿠키는 안먹어

maxlen = max(len(x) for x in combinations)
maxcookies = sorted(list(x for x in combinations if len(x) == maxlen))
print(maxcookies)
print(maxcookies[k - 1])