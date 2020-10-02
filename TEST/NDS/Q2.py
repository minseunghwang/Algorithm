def solution(goods, boxes):
    answer = 0

    g = sorted(goods)
    b = sorted(boxes)
    gl = len(goods)
    bl = len(boxes)
    j = 0
    print(g)
    print(b)

    for i in range(gl):
        while(j<bl):
            if g[i] <= b[j]:
                answer += 1
                j += 1
                break
            j += 1
    return answer

goods = [5,3,7]
goods = [1,2]
goods = [3,8,6]
# goods = [10,11,12,13,14]

boxes = [3,7,6]
boxes = [2,3,1]
boxes = [5,6,4]

# boxes = [3,4,5,6,7]

print(solution(goods,boxes))