import sys
import itertools
input = sys.stdin.readline
a,b = map(int,input().split())
x = [i for i in range(1,a+1)]
s = list(itertools.permutations(x,b))
for i in range(len(s)):
    print(*s[i])