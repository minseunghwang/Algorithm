def countSwaps(a):
    answer = 0
    for i in range(len(a)):
        for j in range(0,len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                answer += 1
                print(a)

    print(f'Array is sorted in {answer} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    return answer


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)


'''
input
3
3 2 1

output
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
'''