import sys
n = int(sys.stdin.readline().rstrip().rstrip())
c = 0
d = 1
for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    c = a * b
    while a!=0:
        b = b%a
        a,b = b,a
    d = b
    print(c//d)