from string import ascii_lowercase

def solution(sentence):
    answer = ""

    alpha_list = list(ascii_lowercase)
    # print(alpha_list)

    sen = sentence.lower().split()
    print(sen)
    for i in sen:
        for j in i:
            if j in alpha_list:
                alpha_list.remove(j)

    if len(alpha_list) == 0:
        return "perfect"

    return "".join(alpha_list)

sentence ="His comments came after Pyongyang announced it had a plan to fire four missiles near the US territory of Guam.";
sentence ="Jackdaws love my big sphinx of quartz";
print(solution(sentence))