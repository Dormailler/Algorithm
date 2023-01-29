def solution(box, n):
    answer = 1
    count = 0
    for i in range(len(box)):
        if box[i] >= n :
            answer *= (box[i] // n)
        else:
            count = 1
    if count == 1:
        answer = 0
    return answer