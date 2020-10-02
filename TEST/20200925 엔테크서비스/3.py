def solution(histogram):
    answer = 0

    l = len(histogram)
    for i in range(l):
        for j in range(i + 2, l):
            now = (abs(j - i) - 1) * min(histogram[i], histogram[j])
            print(i,j,now)
            if now > answer:
                answer = now

    return answer

histogram = [6, 5, 7, 3, 4, 2]
print(solution(histogram))