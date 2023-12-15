def solution(n, stations, w):
    answer = 0 
    p = 0
    arr = []
    for i in stations:
        arr.append([i-w,i+w])
    for i in arr:
        answer += -(-(i[0]-1-p)//(w*2+1))
        p = i[1]
    if p < n:
        answer += -(-(n-p)//(w*2+1))
    return answer