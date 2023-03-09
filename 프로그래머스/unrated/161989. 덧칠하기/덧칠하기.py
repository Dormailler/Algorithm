def solution(n, m, section):
    answer = 0
    stack = []
    num = m
    for i in section:
        if stack == []:
            stack.append(i)
            continue
        if (i - stack[-1]+1) <= num :
            num -= (i-stack[-1])
            stack.pop()
        else:
            num = m
            stack.pop()
            answer += 1
        stack.append(i)
    answer += 1
    return answer