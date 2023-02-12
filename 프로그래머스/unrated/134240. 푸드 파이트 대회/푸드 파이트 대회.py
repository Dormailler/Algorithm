def solution(food):
    answer = '0'
    for i in range(len(food)-1,0,-1):
        s = str(i) * (food[i]//2)
        answer =  s + answer + s
    return answer