import sys
n = int(sys.stdin.readline())
deck = []
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push_front':
        deck.insert(0,a[1])
    elif a[0] == 'push_back':
        deck.append(a[1])
    elif a[0] == 'pop_front':
        if(deck == []):
            print(-1)
            continue
        print(deck.pop(0))
    elif a[0] == 'pop_back':
        if(deck == []):
            print(-1)
            continue
        print(deck.pop())
    elif a[0] == 'size':
        print(len(deck))
    elif a[0] == 'empty':
        if(deck == []):
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if(deck == []):
            print(-1)
        else:
            print(deck[0])
    elif a[0] == 'back':
        if(deck == []):
            print(-1)
        else:
            print(deck[-1])