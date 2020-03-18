import sys

sys.stdin = open('data/1213.txt','r',encoding='UTF8')

a = []

for i in sys.stdin:
    a.append(str(i))

print(a[2].count('ti'))
print(type(a[2]))
print(a[2])

for test_case in range(1, 2):
    # trash = input()?
    keyword = 'ti'
    sentence = a[2]

    print(sentence.count(keyword))