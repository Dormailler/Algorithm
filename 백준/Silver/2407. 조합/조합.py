import sys
n,m = map(int,sys.stdin.readline().rstrip().rstrip().split())
a,b = n,m
out = 1
for i in range(m+1,n+1):
    out *= i
for i in range(1,n-m+1):
    out //= i
print(out)