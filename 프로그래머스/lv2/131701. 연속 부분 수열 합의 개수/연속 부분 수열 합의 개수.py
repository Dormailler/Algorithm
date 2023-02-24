def solution(elements):
    stack = []
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            if i+j > len(elements):
                stack.append(sum(elements) - sum(elements[i+j-len(elements):j]))
            else:
                stack.append(sum(elements[j:i+j]))
    return len(set(stack))