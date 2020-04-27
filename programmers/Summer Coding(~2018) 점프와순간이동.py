def solution(n):
    ans = 0

    while n != 0:
        print(n)
        if n%2 == 0:
            n = n//2
        else:
            n-=1
            ans += 1

    return ans

def solution2(n):
    ans = 0
    print(bin(n).count('1'))
    return ans


n = 5
n = 6
# n = 5000

print(solution2(n))

