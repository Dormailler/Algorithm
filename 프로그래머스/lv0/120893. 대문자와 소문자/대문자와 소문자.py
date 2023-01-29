def solution(my_string):
    my_string = list(my_string)
    answer = [0] * len(my_string)
    for i in range(len(my_string)):
        for j in range(65,91):
            if my_string[i] == chr(j):
                answer[i] = chr(j + 32)
        for k in range(97,123):
            if my_string[i] == chr(k):
                answer[i] = chr(k - 32)
    answer = ''.join(answer)
    return answer