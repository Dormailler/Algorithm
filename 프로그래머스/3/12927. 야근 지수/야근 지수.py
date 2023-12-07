import heapq

def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        max_work = heapq.heappop(works)
        if max_work == 0:
            break
        heapq.heappush(works, max_work + 1)

    answer = sum(w ** 2 for w in works)
    return answer if answer >= 0 else 0