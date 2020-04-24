def solution(begin, target, words):
    answer = 0
    visit = [0] * len(words)

    if target not in words:
        return 0

    def bfs(q, target):
        while q:
            print(q)
            p, cnt = q.pop(0)
            level = 0
            for a, b in zip(p, target):
                if a == b:
                    level += 1

            if p in words:
                if p == target:
                    return (p, cnt)
                visit[words.index(p)] = 1
            print(level, visit)
            for c, word in enumerate(words):
                sim, sim2 = 0, 0
                for i, w in zip(p, word):
                    if visit[c] != 1 and i == w:
                        sim += 1
                if sim == 2:
                    for t, w in zip(target, word):
                        if t == w:
                            sim2 += 1
                    if sim2 >= level:
                        q.append([word, cnt + 1])

        return (0, 0)

    q = [[begin, 0]]
    trash, answer = bfs(q, target)

    return answer


begin = 'hit'
target = 'cog'
# words = ['hio', 'hho', 'hht', 'hhh']
words = ['hot', 'dot','cot', 'dog', 'lot', 'log', 'cog']
print(solution(begin, target, words))

# print(words.index('cog'))