import sys
import math
n,s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
stack = []
for i in range(n):
    stack.append(abs(a[i] - s))
out = stack[0]
for i in range(1,n):
    out = math.gcd(stack[i],out)
print(out)