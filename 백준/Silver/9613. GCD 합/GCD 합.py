import sys
n = int(sys.stdin.readline())

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    out = 0
    j = 1
    for i in range(1,a[0]+1):
        gcd = 0
        while i+j < len(a):
            for x in range(min(a[i],a[i+j]),0,-1):
                if a[i] % x ==0 and a[i+j] % x== 0:
                    gcd = x
                    break
            out += gcd 
            j += 1
        j = 1
    print(out)