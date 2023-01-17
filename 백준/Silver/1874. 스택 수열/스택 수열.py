import sys
n = int(sys.stdin.readline())
cnt = 1
su = [] 
pr = []
for i in range(n):
    a = int(sys.stdin.readline())
    while(cnt <= a):
            su.append(cnt)
            pr.append('+')
            cnt += 1
    if a == su[-1]:
            su.pop()
            pr.append('-')
    else: 
        print('NO')
        exit()
  
for i in range(len(pr)):
    print(pr[i])