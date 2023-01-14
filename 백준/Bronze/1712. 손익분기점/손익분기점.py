a,b,c = map(int,input().split())
k = 0
if b>=c:
    print(-1)
else:
    k = a//(c-b)+1
    print(k)
