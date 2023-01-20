import sys
s = list(sys.stdin.readline().rstrip())
for i in range(len(s)):
    for j in range(97,123):
        if s[i] == chr(j):
            if j+13 > 122:
                s[i] = chr(j-13)
            else:
                s[i] = chr(j+13)
            break
    for x in range(65,91):
        if s[i] == chr(x):
            if x+13 > 90:
                s[i] = chr(x-13)
            else:
                s[i] = chr(x+13)
            break
for i in range(len(s)):
    print(s[i],end='')