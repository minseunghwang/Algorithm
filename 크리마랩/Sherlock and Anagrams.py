def sherlockAndAnagrams(s):

    q_len = 1
    q = s[0:q_len]
    while True:
        for i in range(len(s)):
            for j in q:
                if j not in q:
                    break
            




q = int(input())
for q_itr in range(q):
    s = input()
    print(sherlockAndAnagrams(s))