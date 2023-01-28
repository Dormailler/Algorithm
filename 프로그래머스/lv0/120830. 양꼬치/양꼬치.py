def solution(n, k):
    a = n
    while a >= 10:
        a -= 10
        k -= 1 
    answer = 12000 * n + 2000*k
    return answer