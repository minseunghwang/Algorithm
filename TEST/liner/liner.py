def solution(inputString):
    answer = 0
    stack = []
    for i in inputString:
        if i == '(' or i == '{' or i =='[' or i == '<':
            stack.append(i)
        if i == ')' or i == '}' or i ==']' or i == '>':
            if len(stack) == 0:
                return -1
            for cnt, j in enumerate(stack):
                if (j == '(' and i ==')') or (j == '{' and i == '}') or (j == '[' and i == ']') or (j == '<' and i == '>'):
                    stack.pop(cnt)
                    answer += 1
    if len(stack) != 0:
        return -1

    return answer


inputString = 'line[plus]'
inputString = 'if (Count of eggs is 4.) {Buy milk.}	'
inputString = '[(])'
inputString = 'Hello, world!'
print(solution(inputString))
