n = int(input())
if n%5 == 0:
    k = n//5
elif (n%5)%3 ==0:
    k = n//5 + n%5//3
elif (n%3)%5 == 0 and n%3!=0:
    k = n//3 + n%3//5
else:
    for i in range(2,5):
        if (n - (3*i))%5 == 0:
            if(n-(3*i)<0):
                k = -1
                break
            k = (n -(3*i))//5 + i
            break
        elif n%3 == 0:
            k = n//3
        else:
            k = -1
print(k)