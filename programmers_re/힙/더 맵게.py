import heapq
def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)


    return heap

scoville = [1, 2, 3, 9, 10, 12]
K = 100

print(solution(scoville, K))