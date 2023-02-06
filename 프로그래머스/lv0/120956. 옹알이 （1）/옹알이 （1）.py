def solution(babbling):
    answer = 0  
    stack = ['aya','ye','woo','ma']
    for a in babbling:
        for b in stack:
            if b in a:
                a = a.replace(b,"1")
        if a.isdigit():
            answer += 1
    return answer