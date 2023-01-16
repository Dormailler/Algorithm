b = []
for i in range(5):
    a = int(input())
    b.append(a)
b = sorted(b)
print(int(sum(b)/5))
print(b[2])