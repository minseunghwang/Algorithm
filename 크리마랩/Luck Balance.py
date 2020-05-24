def luckBalance(k, contests):

    answer = 0
    contests.sort(key=lambda x:x[0],reverse=True)
    # print(contests)
    for i,j in contests:
        if j == 0:
            answer += i
        else:
            if k > 0:
                answer += i
                k -= 1
            else:
                answer -= i
    print(answer)




if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    print(luckBalance(k, contests))