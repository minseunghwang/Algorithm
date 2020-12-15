def solution(skill, skill_trees):
    answer = 0
    a_skill = [skill[:i] for i in range(len(skill)+1)]
    print(a_skill)
    for skill_tree in skill_trees:
        temp = ""
        for i in skill_tree:
            if i in skill:
                temp += i
        if temp in a_skill:
            answer += 1


    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))