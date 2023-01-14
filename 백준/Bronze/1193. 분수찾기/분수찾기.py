n = int(input())
c = 4
s = 1
k = 1
d = 1
while(s+c<n):
    s += c
    c += 4
    k += 1

a = k
b = k

for i in range(s,n):
    if(d%2 == 1 and a == 1):
        b+=1
        d+=1
    elif(d%2 == 0 and b == 1):
        a+=1
        d+=1
    elif(d%2 == 1):
        a -= 1
        b += 1
    elif(d%2 == 0):
        b -= 1
        a += 1
print('{}/{}'.format(a,b))