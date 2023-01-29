def solution(numbers, direction):
    answer = [0] * len(numbers)
    if direction == 'right':
        for i in range(len(numbers)):
            answer[i] = numbers[i-1]
    else:
        for i in range(-1,len(numbers)-1):
            answer[i] = numbers[i+1]
    return answer