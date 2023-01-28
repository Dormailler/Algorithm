def solution(slice, n):
    answer = 1
    a = n
    while slice < a:
        a -= slice
        answer += 1
    return answer