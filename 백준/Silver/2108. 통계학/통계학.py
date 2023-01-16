import sys
from collections import Counter
n = int(sys.stdin.readline())
b = []
most = 0
cnt = 1
for i in range(n):
    a = int(sys.stdin.readline())
    b.append(a)
b = sorted(b)
c = Counter(b).most_common()
d = [i for i in c]
if n == 1 or len(c) == 1:
    most = b[0]
elif d[0][1] > d[1][1]:
    most = d[0][0]
else:
    most = d[1][0]
print(round(sum(b) / n))
print(b[n//2])
print(most)
print(max(b)-min(b))