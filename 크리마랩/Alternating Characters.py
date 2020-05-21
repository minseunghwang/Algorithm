def alternatingCharacters(s):
    answer = 0

    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            answer += 1

    return answer


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()
        print(alternatingCharacters(s))