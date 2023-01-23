n = int(input())
a = list(map(int, input().split()))
stack = []
stack.append(a[0])
for i in range(len(a)-1,0,-1):
    if a[i]>= 0 and a[i-1] >=0 or a[i] > abs(a[i-1]):
        a[i-1] = a[i] + a[i-1]
        stack.append(a[i-1])
        stack.append(a[i])
    else:
        stack.append(a[i])
print(max(stack))