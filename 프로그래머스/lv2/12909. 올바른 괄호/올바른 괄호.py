def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(1)
        else:
            if stack == []:
                return False
            stack.pop()
    if stack == []:
        return True
    else:
        return False