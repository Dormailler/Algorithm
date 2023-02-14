def solution(babbling):
    sound = ['aya','ye','woo','ma']
    no = ['ayaaya','yeye','woowoo','mama']
    answer = 0
    for i in babbling:
        a = 0
        for j in no:
            if j in i:
                a = 1
                break
        if a == 1:
            continue
        for k in sound:
            if k in i:
                i = i.replace(k,'1')
        if i.isdigit():
            answer += 1                 
    return answer