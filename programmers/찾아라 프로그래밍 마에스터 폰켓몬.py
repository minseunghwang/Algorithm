def solution(nums):

    l = len(nums) // 2
    a = len(list(set(nums)))

    if l < a:
        return l
    return a

# nums = [3,1,2,3]
nums = [3,3,3,2,2,4]
# nums = [3,3,3,2,2,2]
# nums = [1,1,1,1,1,2]
nums = [1,2,3,4,5,6]

# print(solution(nums))

# dup_list = [[1,2],[2,1],[1]]
# remove_dup = list(set(map(tuple,dup_list)))
# print(remove_dup)