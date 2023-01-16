n =int(input())
b = []
for i in range(n):
    a = int(input())
    b.append(a)
b = sorted(b)
for i in range(n):
    print(b[i])