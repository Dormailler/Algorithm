def solution(my_string):
    s = my_string.lower()
    s = list(s)
    s.sort()
    return ''.join(s)