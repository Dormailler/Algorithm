import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    a = sys.stdin.readline().split()
    for i in range(len(a)):
        b= list(a[i])
        for i in range(len(b)-1,-1,-1):
            print(b[i],end='')
        print(end=' ')
    print()