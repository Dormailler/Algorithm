import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().rstrip().split()))
c = Counter(a)
out = [-1 for i in range(n)]
stack = [0]
for i in range(1,n):
    while stack and c[a[stack[-1]]] < c[a[i]]:
        out[stack.pop()] = a[i] 
    stack.append(i)
print(*out)