n = int(input())
s = 1 # 2*1 개수
b = 1
while n-(2*s)>0:
    a = 1
    x = 0 #
    r = 0
    c = s
    while n-s-x >0:
        a *= n-s-x
        x += 1
    while n-(2*s)-r >0:
        a //= n-(2*s)-r
        r += 1
    while c > 0 :
        a //= c
        c -= 1
    b += int(a)    
    s +=1
if n%2 ==0:
    b+=1
print(b%10007)