import copy

def solution(stones, k):
    _min, _max = 0, max(stones)
    while _min <= _max:
        mid = (_max + _min) // 2
        temp = copy.deepcopy(stones)
        print(_max, _min, temp,mid)

        for i in range(len(temp)):
            temp[i] -= mid

        cnt = 0
        check = False
        for i in range(len(temp)):

            if temp[i] <= 0:
                cnt += 1
            else :
                cnt = 0

            if cnt > k:
                check = True
                break

        if check is True:
            _max = mid -1
        else :
            _min = mid +1

    return _min

# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones = [1,2,4,1,2,3,4,100,156,575,159,446,854]
k = 3

print(solution(stones, k))