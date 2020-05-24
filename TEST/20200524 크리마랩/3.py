def longestChain(words):

    visit = [0] * words_count
    for c in range(len(words)):
        cnt = 0
        visit[c] = 1
        print(findword(words[c],cnt,visit))


def findword(word,cnts,v):
    print(word,cnts,v)
    for i in range(len(words)):
        print('i',i)
        if word in words[i] and word != words[i] and v[i] != 1:
            print('if')
            v[i] = 1
            findword(words[i],cnts+1,v)
    return cnts








'''
6
a
b
ba
bca
bda
bdca
'''


if __name__ == '__main__':
    words_count = int(input().strip())
    words = []
    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = longestChain(words)