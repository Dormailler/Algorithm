def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3,reverse=True)
    for i in range(len(numbers)):
        answer += str(numbers[i])
    if int(answer) == 0:
        return '0'
    return answer