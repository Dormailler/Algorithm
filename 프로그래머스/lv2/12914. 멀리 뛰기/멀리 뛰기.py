def solution(n):
    stack = [0] * (n+4)
    stack[1] = 1
    stack[2] = 2
    for i in range(3,n+1):
        stack[i] = stack[i-1] + stack[i-2]
    return stack[n] % 1234567