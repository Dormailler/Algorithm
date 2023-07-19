def solution(my_string, is_prefix):
    if is_prefix in my_string:
        if my_string.index(is_prefix) == 0:
            return 1
    return 0
            
        