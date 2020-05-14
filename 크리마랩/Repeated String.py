def repeatedString(s, n):
    a = 0
    if n%len(s) != 0:
        a = s[:n % len(s)].count('a')
    return (s.count('a') * (n // len(s))) + a





s = 'aba'
n = 10

print(repeatedString(s,n))