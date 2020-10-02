from collections import defaultdict
user_input = input()

def solution(user_input):
    answer = []
    d = defaultdict(str)
    for i in user_input.split():
        if d.get(i) == False:
            d[i] = compute(int(i))



    return " ".join(answer)
print(solution(user_input))
