def extraLongFactorials(n):
    if n == 1:
        return 1
    return n * extraLongFactorials(n-1)


n = int(input())

print(extraLongFactorials(n))