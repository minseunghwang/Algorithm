def solution(nums):
    answer = 0
    import itertools

    maxi = sum(nums)
    tf = [True] * (maxi+1)
    tf[0],tf[1] = False , False

    for i in range(2,(maxi) + 1):
        print(i,'i')
        if tf[i] == True:
            for j in range(i+i,maxi,i):
                tf[j] = False
    print(len(tf),tf)

    for i in itertools.combinations(nums,3):
        print(sum(i),'엥')
        if tf[sum(i)] == True:
            answer += 1

    return answer


### for else문 간지나게 쓰네

def solution2(nums):
    answer = 0
    import itertools

    for i in itertools.combinations(nums,3):
        cand = sum(i)
        for j in range(2,cand):
            if cand % j == 0:
                break
        else :
            answer += 1
        print(cand, answer)
    return answer



nums = [1,2,3,4]
nums = [1,2,7,6,4]
# nums = [1,2,3]
print(solution2(nums))