n = int(input())
m = int(input())
s = list(input())
nl = (2*n)+1
print(s)
answer = 0
temp = s[:nl]
for i in range(m-nl+1):
    for j in range(len(temp)-2):
        print(temp)
        if temp[j] == 'I' and temp[j+1] == 'O' and temp[j+2] == 'I':
            answer += 1
    temp

print(answer)


# 1 IOI
# 13
# OOIOIOIOIIOII