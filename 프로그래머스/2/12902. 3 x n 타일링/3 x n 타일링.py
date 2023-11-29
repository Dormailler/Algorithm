def solution(n):
    if n %2 == 1 or n < 2:
        return 0
    answer = [0,3,11]
    for i in range(5000):
        answer.append(answer[-1]*4-answer[-2])

    return answer[n//2] % 1000000007