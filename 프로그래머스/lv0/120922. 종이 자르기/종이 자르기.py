def solution(M, N):
    n = min(M,N)
    m = max(M,N)
    answer = (n-1) + n*(m-1)
    return answer