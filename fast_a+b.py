import sys
a = int(sys.stdin.readline().rstrip())
for i in range(a):
    c,d = map(int,sys.stdin.readline().rstrip().split(' '))
    print(c+d)