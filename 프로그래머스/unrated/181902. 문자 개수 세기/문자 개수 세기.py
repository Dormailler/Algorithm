def solution(my_string):
    answer = [0]*52
    val = 0
    for i in range(len(my_string)):
        val = ord(my_string[i])
        if val < 97:
            answer[val-65] += 1
        else:
            answer[val-71] += 1
    return answer