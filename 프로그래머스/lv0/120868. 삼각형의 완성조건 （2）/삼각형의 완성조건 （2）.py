def solution(sides):
    answer = 0
    for i in range(1,sum(sides)):
        if max(sides) < sum(sides) - max(sides) + i:
            answer += 1
    return answer