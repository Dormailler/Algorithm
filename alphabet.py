s = input()
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
sum = 0
for i in range(len(a)):
    if a[i] in s:
        sum = sum+s.count(a[i])
        s = s.replace(a[i],' ')
s = s.replace(' ','')
sum = sum+ len(s.strip())
print(sum)