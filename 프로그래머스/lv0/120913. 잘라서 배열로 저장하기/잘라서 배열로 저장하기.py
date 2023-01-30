def solution(my_str, n):
    answer = []
    i = 0
    j = n
    while j < len(my_str):
        answer.append(my_str[i:j])
        i += n 
        j += n
    answer.append(my_str[i:])
    return answer