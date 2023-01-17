import sys
n = int(sys.stdin.readline())
que = []
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        que.append(a[1])
    elif a[0] == 'pop':
        if(que == []):
            print(-1)
            continue
        print(que.pop(0))
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':
        if(que == []):
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if(que == []):
            print(-1)
        else:
            print(que[0])
    elif a[0] == 'back':
        if(que == []):
            print(-1)
        else:
            print(que[-1])