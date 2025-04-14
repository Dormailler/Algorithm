def solution(players, m, k):
    answer = 0
    arr = [0 for _ in range(len(players) + k)]
    for i,v in enumerate(players):
        if v >= (arr[i] + 1) * m:
            diff = v // m - arr[i]
            answer += diff
            for j in range(i,i+k):
                arr[j] += diff
    return answer