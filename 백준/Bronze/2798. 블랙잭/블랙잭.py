from itertools import combinations as com
a,b = map(int,input().split())
s = list(map(int,input().split()))
c = list(com(s,3))
stack = []
m = abs(b - sum(c[0]))
for i in range(len(c)):
    if sum(c[i]) > b:
        continue
    else:
        m = min(m,abs(b-sum(c[i])))
print(b-m)
