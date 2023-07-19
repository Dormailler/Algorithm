def solution(numbers, n):
    num = 0
    for i in numbers:
        num += i
        if num > n:
            break
    return num