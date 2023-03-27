from collections import deque
def solution(order):
    order = deque(order)
    answer = 0
    stack = []
    for box in range(len(order)):
        if box+1 == order[0]:
            order.popleft()
            answer += 1
        else:
            stack.append(box+1)
        while stack!=[] and order != [] and stack[-1] == order[0]:
            order.popleft()
            stack.pop()
            answer += 1
    return answer