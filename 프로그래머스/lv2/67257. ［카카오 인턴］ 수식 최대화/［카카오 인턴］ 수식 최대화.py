import re
from itertools import permutations as c
def solution(expression):
    result = 0
    t = list(c(['+','-','*'],3))
    for i in t:
        num = re.split("[+\-*]+",expression)
        calc = re.findall("[+\-*]",expression)
        for j in i:
            n = 0
            for x in range(len(calc)):
                if calc[x-n] == j:
                    calc.pop(x-n)
                    num[x-n] = eval(str(num[x-n]) + j + str(num.pop(x-n+1)))
                    n += 1
        result = max(result,abs(num[0]))            
    return result