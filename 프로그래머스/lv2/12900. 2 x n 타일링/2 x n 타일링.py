def solution(n):
    stack = [0] *(n+1)
    stack[1] = 1
    stack[2] = 2
    for i in range(3,len(stack)):
        stack[i] = (stack[i-1] + stack[i-2])%1000000007
    return stack[-1]%1000000007