def solution(n, words):
    answer = []
    stack = []
    cnt = 0
    while words:
        q = words.pop(0)
        if q in stack:
            return [(cnt%n)+1, int((cnt/n)+1)]
        if cnt > 0 and len(stack) >0 and stack[-1][-1] != q[0]:
            return [(cnt%n)+1,int((cnt/n)+1)]
        stack.append(q)
        cnt += 1

    return [0,0]



n, words = 3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
n, words = 5,['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
# n, words = 2,['hello', 'one', 'even', 'never', 'now', 'world', 'draw']


print(solution(n,words))