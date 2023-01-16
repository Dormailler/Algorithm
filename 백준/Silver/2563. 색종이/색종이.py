a  = [[0 for i in range(101)] for i in range(101)]
n = int(input())
number = 0
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            a[x+i][y+j] = 1
for i in range(101):
    number += a[i].count(1)
print(number)