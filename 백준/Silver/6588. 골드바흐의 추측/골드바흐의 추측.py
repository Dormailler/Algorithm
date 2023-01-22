import  sys
def sosu(a):
        for j in range(2,int(a**0.5)+1):
            if a%j == 0 and a!=j:
                break
        else:
                return 1

while 1:
    out1 = 0
    out2 = 0
    c = 1
    d = 1   
    a = int(sys.stdin.readline())
    out = 0
    if a == 0:
        break
    for j in range(3,a//2+1,2):       
        c = j
        d = a-j
        if sosu(c) == 1 and sosu(d) == 1:
            out1 = c
            out2 = d
            break 
        
    if out1 == 0 and out2 ==0:
        print("Goldbach's conjecture is wrong.")
    else:
        print('{} = {} + {}'.format(a,out1,out2))