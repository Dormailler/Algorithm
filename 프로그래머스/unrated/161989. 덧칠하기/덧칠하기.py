def solution(n, m, section):
    answer = 0
    stack = []
    num = m
    t = 0
    for i in section:
        if stack == []:
            stack.append(i)
            continue
        if (i - stack[-1]+1-t) <= num :
            num -= (i-stack[-1]+1)
            stack.pop()
            t += 1
        else:
            t = 0
            num = m
            stack.pop()
            answer += 1
        stack.append(i)
    answer += 1
    return answer