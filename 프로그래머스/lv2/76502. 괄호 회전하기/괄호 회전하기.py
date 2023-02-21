def correct(st):
    stack = []
    for i in st:
        stack.append(i)
        if len(stack) < 2:
            continue
        if (ord(stack[-2]) == ord(stack[-1]) - 2) or (ord(stack[-2]) == ord(stack[-1]) - 1):
            stack.pop()
            stack.pop()
    if stack == []:
        return 1
    else:
        return 0
def solution(s):
    answer = 0
    op = ['[','{','(']
    cl = [']','}',')']
    stack = []
    for i in range(len(s)):
        s = s[1:] + s[0]
        answer += correct(list(s))
    return answer
