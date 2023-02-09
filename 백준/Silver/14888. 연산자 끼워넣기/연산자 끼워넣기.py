from itertools import permutations
from collections import deque
n = int(input())
li = list(map(int,input().split()))
cal = list(map(int,input().split()))
a = ['+','-','*','/']
st = []
for i in range(4):
    for j in range(cal[i]):
        st.append(a[i])
ran = list(permutations(st,len(st)))
q = deque(ran)
max_result = -1e9
min_result = 1e9
for i in range(len(ran)):
    l = q.popleft()
    result = li[0]
    for i in range(1,len(li)):
        if l[i-1] == '+':
            result += li[i]
        elif l[i-1] == '-':
            result -= li[i]
        elif l[i-1] == '*':
            result *= li[i]
        elif l[i-1] == '/':
            if result < 0 :
                result = -(abs(result) // li[i])        
            else:
                result //= li[i]
    max_result = max(max_result, result)
    min_result = min(min_result, result)
print(max_result)
print(min_result)