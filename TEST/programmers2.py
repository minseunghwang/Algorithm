def solution(office, r, c, move):
    answer = office[r][c]
    office[r][c] = 0
    l = len(office)

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    idx = 0

    for now in move:
        idx = idx % 4
        if now == 'go' and l > (r+dy[idx]) >= 0 and l > (c+dx[idx]) >= 0 and office[r+dy[idx]][c+dx[idx]] != -1:
            r += dy[idx]
            c += dx[idx]
            answer += office[r][c]
            office[r][c] = 0

        elif now == 'right':
            idx += 1

        elif now == 'left':
            idx -= 1

    return answer


office = [[5,-1,4],[6,3,-1],[2,-1,1]]
r,c = 0,0
move = ['right','go','right','go','left','go','left','left','left','left','left','left','left','left','left','left']
# move = ['go','go','right','go','right','go','left','go','right','right','go','left','go']
print(solution(office, r, c, move))
