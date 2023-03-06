from itertools import combinations as c
def solution(number, k):
    answer = 0
    n = list(map(int,number))
    stack =[]
    temp = 0
    stack = []
    t = 0
    for i in n:
        if k >0:
            if stack == []:
                stack.append(i)
            else:
                while stack[-1] < i:
                    stack.pop()
                    k -= 1
                    if k == 0 or stack == []:
                        break
                stack.append(i)
        else:
            stack.append(i)
    if k > 0:
        stack = stack[:len(stack)-k]
    return ''.join(map(str,stack)) 