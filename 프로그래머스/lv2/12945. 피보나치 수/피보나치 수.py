def solution(n):
    stack = [0] * (n+1)
    stack[1] = 1
    for i in range(2,len(stack)):
        stack[i] = stack[i-1] + stack[i-2]
    return stack[n] % 1234567