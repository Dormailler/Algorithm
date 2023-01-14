a,b,v = map(int,input().split())

k = (v-a) // (a-b)
c = (a-b) * k 
while(1):
    c += a
    if(c >= v):
        break
    c -= b
    k += 1
k = k+1
if(a >= v):
    k = 1
print(k)