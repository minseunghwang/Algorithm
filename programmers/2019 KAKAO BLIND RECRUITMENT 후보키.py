from itertools import combinations

def solution(relation):
    answer = 0

    for cnt in range(len(relation)):
        d = {}
        for i in relation:
            print(i)
            if d.get(i[cnt]) == None:
                d[i[cnt]] = 1
            else:


    print(d)




    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))