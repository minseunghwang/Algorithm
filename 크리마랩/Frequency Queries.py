def freqQuery(queries):
    answer = []
    m = {}

    for query in queries:
        if query[0] == 1:
            if m.get(query[1]):
                m[query[1]] += 1
            else:
                m[query[1]] = 1

        elif query[0] == 2 and m.get(query[1]):
            m[query[1]] -= 1

        elif query[0] == 3:
            print(m)
            for i in m.values():
                if i >= query[1]:
                    answer.append(1)
                    break
            else:
                answer.append(0)
    return answer

q = int(input().strip())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
ans = freqQuery(queries)

print(ans)