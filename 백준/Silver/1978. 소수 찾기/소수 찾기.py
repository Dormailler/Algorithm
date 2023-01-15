n = int(input())
number = 0
a = input().split()
a = [int(x) for x in a]
for x in range(n):
    count = 0
    for i in range(1,a[x]+1):
        if a[x]%i == 0:
            count += 1
    if count == 2:
        number += 1
    count = 0
print(number)