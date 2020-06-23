from itertools import combinations

def solution(relation):
    answer = 0
    flag = True
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        print(tmp_set,i)
    print(1<<len(relation[0]))


    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))