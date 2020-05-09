import copy

def solution(stones, k):
    left,right = 1, max(stones)

    while right >= left:
        mid = (right+left) // 2

        temp = []
        for i in range(len(stones)):
            temp.append(stones[i] - mid)
        print(left,right,temp)

        cnt = 0
        check = False
        for i in range(len(temp)):
            if temp[i] <= 0:
                cnt += 1
            else :
                cnt = 0
            if cnt >= k:
                check = True
                break

        if check is True:
            right = mid -1
        else:
            left = mid + 1

    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
# stones = [1,2,4,1,2,3,4,100,156,575,159,446,854]
k = 3

print(solution(stones, k))