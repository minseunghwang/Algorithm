def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(N):
    answer = [0,0]
    for i in range(2,10):
        s = 1
        for j in str(convert(N,i)):
            if j != '0':
                s *= int(j)
        print(i,s)
        print('answer' , answer)
        print("+==================")
        if answer[1] <= s:
            answer = [int(i),s]
    return answer

N = 14
print(solution(N))


