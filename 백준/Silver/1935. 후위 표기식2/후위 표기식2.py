import sys
n = int(sys.stdin.readline().rstrip())
a = list(sys.stdin.readline().rstrip())
x = 0
y = 0
for i in range(n):
    b = int(sys.stdin.readline().rstrip())
    for j in range(len(a)):
        if a[j] == chr(65+x):
            a[j] = b
    x += 1
for i in range(len(a)):
    if a[y] == '*':
        a[y-2] *= a[y-1]
        a.pop(y)
        a.pop(y-1)
        y -= 1
        continue
    elif a[y] == '/':
        a[y-2] /= a[y-1]
        a.pop(y)
        a.pop(y-1)
        y -= 1
        continue
    elif a[y] == '+':
        a[y-2] += a[y-1]
        a.pop(y)
        a.pop(y-1)
        y -= 1
        continue
    elif a[y] == '-':
        a[y-2] -= a[y-1]
        a.pop(y)
        a.pop(y-1)
        y -= 1
        continue
    y += 1
print('{:.2f}'.format(a[0]))