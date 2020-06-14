from collections import defaultdict
def solution(clothes):
    answer = 1
    h = defaultdict(int)
    for cloth in clothes:
        h[cloth[1]] += 1

    for i in h.values():
        answer *= i+1

    return answer-1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
print(solution(clothes))