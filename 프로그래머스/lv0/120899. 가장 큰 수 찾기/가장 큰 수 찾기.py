def solution(array):
    answer = []
    for i in range(len(array)):
        if array[i] == max(array):
            answer.append(max(array))
            answer.append(i)
    return answer