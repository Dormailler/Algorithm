def solution(num_list, n):
    answer = []
    l = len(num_list) //n
    j = 0
    for i in range(1,l+1):
        answer.append(num_list[j:n*i])
        j += n
    return answer