def solution(flowers):
    f = set()
    for flower in flowers:
        for i in range(flower[0],flower[1]):
            f.add(i)

    return len(f)

flowers = [[2, 5], [3, 7], [10, 11]]
flowers = [[3, 4],[4, 5], [6, 7], [8, 10]]
print(solution(flowers))