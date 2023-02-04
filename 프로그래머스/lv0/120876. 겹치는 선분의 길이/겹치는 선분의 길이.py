def solution(lines):
    stack = [0 for i in range(300)]
    num = 0
    for i in lines:
        for j in range(i[0],i[1]):
            stack[j] += 1
    for i in stack:
        if i >= 2:
            num += 1
    return num