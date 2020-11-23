
def find_empty_room(x,rooms):
    if x not in rooms:
        rooms[x] = x + 1
        return x
    p = find_empty_room(rooms[x],rooms)
    rooms[x] = p + 1
    return p


def solution(k, room_number):
    answer = []
    rooms = {}
    for each_room in room_number:
        empty_room = find_empty_room(each_room, rooms)
        answer.append(empty_room)
        print(answer)

    return answer

k = 100
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))