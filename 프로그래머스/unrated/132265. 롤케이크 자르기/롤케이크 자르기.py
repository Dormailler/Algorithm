from collections import Counter as c
from collections import deque
def solution(topping):
    a = set()
    l = c(topping)
    answer = 0
    for i in topping:
        l[i] -= 1
        if l[i] == 0:
            del l[i]
        if i not in a:
            a.add(i)
        if len(a) == len(l):
            answer += 1
    return answer