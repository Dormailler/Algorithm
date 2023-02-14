def solution(X, Y):
    x = set(X)
    y = set(Y)
    li = []
    for i in x:
        if i in y:
            li.append(i)
    stack = []
    for i in li:
        stack.append(i * min(X.count(i),Y.count(i)))
    if stack == []:
        stack.append('-1')
    if any([int(stack[i]) for i in range(len(stack))]) == False:
        stack = ['0']
    stack = ''.join(sorted(stack,reverse=True))
    return stack