import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().rstrip().split()))
out = [-1] * n
stack = [0]
for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:
        out[stack.pop()] = a[i]
    stack.append(i)
print(*out)