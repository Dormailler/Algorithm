def solution(arr):
    n = 1
    while n < len(arr):
        n *= 2
    while len(arr) != n:
        arr.append(0)
    return arr