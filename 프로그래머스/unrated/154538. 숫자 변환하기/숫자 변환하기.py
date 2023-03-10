from collections import deque 
def solution(x, y, n):
    answer = [0]*1000001
    stack = deque()
    stack.append(x)
    answer[x] = 1
    while stack:
        x = stack.popleft()
        if 0 <= x + n <= 1000000 and answer[x + n] == 0:
            answer[x + n] = answer[x] + 1
            stack.append(x + n)
        if 0 <= x * 2 <= 1000000 and answer[x * 2] == 0:
            answer[x * 2] = answer[x] + 1
            stack.append(x * 2)
        if 0 <= x * 3 <= 1000000 and answer[x * 3] == 0:
            answer[x * 3] = answer[x] + 1
            stack.append(x * 3) 
    return answer[y] - 1