n = int(input())
stack = [0] *(n+5)
stack[1] = 1
stack[2] = 1
stack[3] = 2
for i in range(2,n+1):
    stack[i] = stack[i-1] + stack[i-2]
print(stack[n])