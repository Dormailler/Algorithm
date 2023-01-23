n = int(input())
b = 1
x = 0
y = 2
z = 1
q = 1
while n-(2*x)>0:
    s = 1+x
    while n-(2*s)>0:
        a = 1
        x = 0 #
        r = 0
        c = s
        while n-s-x >0:
            a *= (n-s-x)
            x += 1
        while n-(2*s)-r >0:
            a //= (n-(2*s)-r)
            r += 1
        while c > 0 :
            a //= c
            c -= 1
        b += int(a * y)  
        y *= 2
        s += 1  
    x += 1
if n%2 ==0 :
    z = n//2
    for i in range(z):
        q *= 2 
if q>1:
    b += q
print(b%10007)