from itertools import permutations as p
def solution(spell, dic):
    a = list(p(spell))
    for i in a:
        if ''.join(i) in dic:
            return 1
    return 2
    