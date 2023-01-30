def solution(numbers, k):
    n = 0
    for i in range(k-1):
        n += 2
    while n >= len(numbers):
        n -= len(numbers)
    return numbers[n]