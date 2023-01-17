import sys
stack = []
li =[]
out = []
a = sys.stdin.readline().rstrip()
b = list(a)
num = 0
for i in range(len(a)):
    if a[i] == '<':
        if li != []:
            c = ''.join(li).split()
            for x in range(len(c)):
                for j in range(len(c[x])-1,-1,-1):
                    print(c[x][j],end='')
                if x < len(c)-1:
                    print(end=' ')
            li.clear()
        num = 1
    if num == 1:
        print(a[i],end='')
        if a[i] == '>':
            num = 0
    else:
        li.append(a[i])
if li != []:
    c = ''.join(li).split()
    for i in range(len(c)):
        for j in range(len(c[i])-1,-1,-1):
            print(c[i][j],end='')
        if i < len(c)-1:
            print(end=' ')