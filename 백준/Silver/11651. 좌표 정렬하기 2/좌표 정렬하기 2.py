import sys
n = int(sys.stdin.readline())
li = []
fli =[]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    li.append([b,a])
li.sort()
for i in range(n):
    fli.append([li[i][1],li[i][0]])
for i in range(n):
    print(fli[i][0],fli[i][1])