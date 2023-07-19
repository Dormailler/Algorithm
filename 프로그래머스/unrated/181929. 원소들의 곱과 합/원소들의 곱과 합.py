def solution(num_list):
    mul = 1
    s = 0
    for i in num_list:
        mul *= i
        s += i
    if mul < s**2 :
        return 1
    return 0