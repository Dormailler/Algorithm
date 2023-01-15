n = int(input())

for i in range(n):
    counth = 0
    countl = 1
    a,b,c = map(int,input().split())
    for i in range(c):
        counth += 1
        if counth == a+1:
            counth = 1
            countl += 1 
        
         
    if(countl<10):
        print('{}0{}'.format(counth,countl))
    else:
        print('{}{}'.format(counth,countl))