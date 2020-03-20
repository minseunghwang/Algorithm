f = open('data/1223.txt','r',encoding='UTF-8').readlines()

stack = []
result = ''
result2 = []
for i in f[1][:-1]:
    if i >= '0' and i <= '9':
        result += i
        result2.append(i)
    else:
        if len(stack) == 0:
            stack.append(i)
        else:
            while (len(stack) != 0) and ((stack[-1] == '*' and i == '+') or (stack[-1] == '*' and i == '*') or (stack[-1] == '+' and i == '+')):
                a = stack.pop()
                result += a
                b = result2.pop()
                c = result2.pop()
                result2.append(str(eval(c+a+b)))
            stack.append(i)
            if stack[-1] == '+' and i == '*':
                stack.append(i)

while len(result2) != 1:
    a = stack.pop()
    b = result2.pop()
    c = result2.pop()
    result2.append(str(eval(c+a+b)))
print(''.join(result2))


# result3 = 'abcdefg'
# result3 = result3[:-2]
# print(result3)
