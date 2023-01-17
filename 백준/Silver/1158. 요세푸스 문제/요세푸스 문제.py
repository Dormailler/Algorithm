import sys
n,b = map(int,sys.stdin.readline().split())
num = [i for i in range(1,n+1)]
a = 0
out = []
for i in range(n):
    a += b-1
    while(a>=len(num)):
        a -= len(num)
    out.append(num.pop(a))
print('<',end='')
for i in range(len(out)):
    print(out[i],end='')
    if i == len(out)-1:
        break
    print(',',end=' ')
print('>',end='')
