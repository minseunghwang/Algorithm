user_input = input()

def solution(user_input):
    for i in range(len(user_input)):
        if user_input[-1] == '1':
            return False;
        if user_input[i] != '1' and user_input[i] != '2':
            return False
        if i<len(user_input)-1 and user_input[i]=='1' and user_input[i+1] != '2':
            return False
    return True;

print(solution(user_input))
