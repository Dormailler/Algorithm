import math
def solution(numer1, denom1, numer2, denom2):
    numer1 *= denom2
    numer2 *= denom1
    new_numer = numer1 + numer2
    new_denom = denom1 * denom2
    gcd = math.gcd(new_numer,new_denom)
    return [new_numer//gcd,new_denom//gcd]