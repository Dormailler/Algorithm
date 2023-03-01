def solution(land):
    answer = 0
    for i in range(len(land)):
        if i == 0:
            continue
        for j in range(4):
            land[i][j] += max(land[i-1][0:j]+land[i-1][j+1:4])
    return max(land[-1])