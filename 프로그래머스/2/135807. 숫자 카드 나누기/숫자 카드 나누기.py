import math
from functools import reduce

def solution(arrayA, arrayB):
    answer = []
    a = reduce(math.gcd,arrayA)
    b = reduce(math.gcd,arrayB)
    ml = max(a,b)
    l = len(arrayA)
    for i in range(2,ml+1):
        k = 0
        isk = 0
        n = 0
        m = 0
        for num in arrayA:
            if num % i == 0:
                k += 1
                isk = 1
            else:
                if isk == 1:
                    n = 1
                    break
        if (k != 0 and k != l) or n == 1:
            continue
        for num in arrayB:
            if num % i == 0:
                if k != 0:
                    m = -1
                    break
                m += 1
        if (k == 0 and m == l) or (k == l and m == 0):
            answer.append(i)

    if answer == [] :
        return 0
    return max(answer)