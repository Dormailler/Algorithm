def solution(my_string, s, e):
    if s == 0:
        return my_string[::-1]
    return my_string[0:s] + my_string[e:s-1:-1] + my_string[e+1:]
