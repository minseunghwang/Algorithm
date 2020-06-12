
def solution(a):
    answer = 0
    a = a.replace('()','0')
    stick = 0
    cstick = 0
    for i in a:
        if i == '(':
            stick += 1
            cstick += 1
        elif i == '0':
            cstick += stick
        else :
            stick -= 1


    return cstick


a= '()(((()())(())()))(())'
print(solution(a))