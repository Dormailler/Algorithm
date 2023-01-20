import sys
s = sys.stdin.readline()
a = [0] * 26
for j in s:
    for i in range(97,123):
        if j == chr(i):
            a[i-97] += 1
print(*a)