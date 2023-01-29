def solution(order):
    answer = 0
    n = list(str(order))
    for i in n:
        if int(i) == 3 or int(i) == 6 or int(i) == 9:
            answer +=1
    return answer