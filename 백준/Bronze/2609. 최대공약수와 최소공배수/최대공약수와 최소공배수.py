import sys
s = list(map(int,sys.stdin.readline().rstrip().split()))
n = 0

for i in range(1,s[0]+1):
    if s[0] % i ==0 and s[1] % i == 0:
        n = i
a = s[0]//n * s[1]
print(n)
print(a)
