for test_case in range(1, 2):
    trash = input()

    sq = input()

    answer = 0

    for i in sq:
        if i > '0' and i <= '9':
            answer += int(i)

    print(f'#{test_case} {answer}')

