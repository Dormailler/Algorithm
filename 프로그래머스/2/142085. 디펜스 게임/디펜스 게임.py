import heapq
def solution(n, k, enemy):
    answer = 0
    att = []
    if k >= len(enemy):
        return len(enemy)
    for i,e in enumerate(enemy):
        heapq.heappush(att,e)
        if len(att) > k:
            n -= heapq.heappop(att)
        if n < 0:
            return i
    return len(enemy)