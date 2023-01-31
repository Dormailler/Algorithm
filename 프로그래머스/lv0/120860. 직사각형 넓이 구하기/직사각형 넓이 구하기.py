def solution(dots):
    answer = 1
    for i in range(1,len(dots)):
        if dots[i][0] == dots[0][0]:
            answer *= abs(dots[i][1] - dots[0][1])
        elif dots[i][1] == dots[0][1]:
            answer *= abs(dots[i][0] - dots[0][0])
    return answer