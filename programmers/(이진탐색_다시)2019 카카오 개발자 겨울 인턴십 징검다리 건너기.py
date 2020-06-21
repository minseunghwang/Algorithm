import copy

def solution(stones, k):
    left,right = 0, max(stones)

    while right > left:
        mid = (left+right)//2

        cnt = 0
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
# stones = [1,2,4,1,2,3,4,100,156,575,159,446,854]
k = 3

print(solution(stones, k))