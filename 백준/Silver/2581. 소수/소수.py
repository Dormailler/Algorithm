minn = int(input())
max = int(input())
number = 0
s = []
for i in range(minn,max+1):
    count = 0
    for j in range(1,i+1):       
        if i%j == 0:
            count += 1
    if count == 2:
        s.append(j)
    count = 0
s = [int(x) for x in s]
if s == []:
    print(-1)
else:
    print(sum(s))
    print(min(s))