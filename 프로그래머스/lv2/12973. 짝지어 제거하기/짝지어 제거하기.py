def solution(s):
    a = list(set(s))
    li = list(s)
    stack = []
    if len(s) % 2 != 0:
        return 0
    for i in a:
        if s.count(i) % 2 != 0:
            return 0
    for i in li:
        stack.append(i)
        if len(stack) < 2:
            continue
        if stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()
    if stack == []:
        return 1
    else:
        return 0