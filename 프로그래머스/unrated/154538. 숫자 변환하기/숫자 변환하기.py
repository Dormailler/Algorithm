from collections import deque 
def solution(x, y, n):
    answer = [0]*1000001
    stack = deque()
    stack.append(x)
    answer[x] = 1
    while stack:
        a = stack.popleft()
        if a + n <= y and answer[a + n] == 0:
            answer[a + n] = answer[a] + 1
            stack.append(a + n)
        if a * 2 <= y and answer[a * 2] == 0:
            answer[a * 2] = answer[a] + 1
            stack.append(a * 2)
        if a * 3 <= y and answer[a * 3] == 0:
            answer[a * 3] = answer[a] + 1
            stack.append(a * 3) 
    return answer[y] - 1