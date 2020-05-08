from itertools import product, combinations
from copy import deepcopy

def solution(user_id, banned_id):
    answer = 0
    candidate = [ [] for _ in range(len(banned_id))]

    cnt = 0
    while banned_id:
        ban = banned_id.pop(0)
        for u_id in user_id:
            if len(u_id) == len(ban):
                for i,j in zip(u_id, ban):
                    if j != '*' and i != j:
                        break
                    if j == '*':
                        continue
                else:
                    candidate[cnt].append(u_id)
        cnt += 1

    print(candidate)
    answer = dfs_check(0, candidate, set(), len(banned_id))

    return answer


check = []
def dfs_check(idx, candidates, arr, length):

    if idx == len(candidates):
        if arr not in check:
            check.append(deepcopy(arr))
        return

    for each_id in candidates[idx]:
        if each_id not in arr:
            arr.add(each_id)
            dfs_check(idx+1, candidates, arr, length)
            arr.remove(each_id)

    return len(check)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned_id = ["fr*d*", "abc1**"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id,banned_id))