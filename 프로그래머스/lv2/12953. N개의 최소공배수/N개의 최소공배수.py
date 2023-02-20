from math import gcd
def solution(arr):
    g = arr[0]
    for i in range(len(arr)):
        g = g*arr[i] // gcd(g,arr[i])
    return g