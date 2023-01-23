n = int(input())
stack = [[0]*10 for i in range(101)]
num = 0
for i in range(1,10):
    stack[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            stack[i][j] = stack[i-1][1]
        elif j == 9:
            stack[i][j] = stack[i-1][8]
        else:
            stack[i][j] = stack[i-1][j-1] + stack[i-1][j+1] 
print(sum(stack[n])% 1000000000)