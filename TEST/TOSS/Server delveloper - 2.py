user_input = input()

def solution(user_input):
    lotto = user_input.split()

    if len(set(lotto)) != 6:
        return False

    if int(lotto[0]) < 1 or int(lotto[-1]) > 45:
        return False

    if sorted(lotto) != lotto:
        return False


    return True



print(solution(user_input))
