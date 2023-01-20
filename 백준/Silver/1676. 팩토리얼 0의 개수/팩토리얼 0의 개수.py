import sys
n = int(sys.stdin.readline().rstrip().rstrip())
fac = 1
zero = 0
for i in range(n-1):
    fac *= n
    n = n-1
while fac:
    if fac%10 == 0:
        zero+=1
    else:
        break
    fac = (fac - fac%10)//10
print(zero)