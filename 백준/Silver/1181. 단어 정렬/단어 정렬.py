import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    li.append(a)
new_li = set(li)
li = list(new_li)
li.sort()
li.sort(key = len)
for i in range(len(li)):
    print(li[i])