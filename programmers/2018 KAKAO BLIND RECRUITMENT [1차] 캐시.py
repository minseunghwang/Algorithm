def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        print(cache, city)
        if city.lower() in cache:
            answer += 1
            cache.pop(cache.index(city.lower()))
        else:
            answer += 5
        cache.append(city.lower())
        if len(cache) > cacheSize:
            cache.pop(0)

    return answer


cacheSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

cacheSize = 3
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
cities = ["Jeju","Pangyo","Jeju","NewYork","Jeju","Jeju","Jeju"]



print(solution(cacheSize, cities))