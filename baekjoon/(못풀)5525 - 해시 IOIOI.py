n = int(input())
m = int(input())
s = list(input())
answer = 0

num = 0
for i in range(m-2):
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        num += 1
        if(num == n):
            answer += 1
            num -= 1
        i += 1
    elif (i >= 1 and s[i-1] == s[i]):
        num = 0

print(answer)

# 3
# 13
# OOIOIOIOIIOII

