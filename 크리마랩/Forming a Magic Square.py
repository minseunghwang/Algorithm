from itertools import permutations

def formingMagicSquare(s):
    answer = 0
    mini = 10000
    for i in permutations(range(1,10)):
        if sum(i[0:3]) == 15 and sum(i[3:6]) == 15 and sum(i[0::3]) == 15 and sum(i[1::3]) == 15 and i[4] == 5:
            summ = 0
            for a,b in zip(s,i):
                summ += abs(a-b)
            mini = min(mini,summ)
    return mini

s = [4, 9, 2, 3, 5, 7, 8, 1, 5]

print(formingMagicSquare(s))
