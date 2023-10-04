def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    for p in callings:
        idx = dic[p]
        front = players[idx - 1]       
        dic[p] -= 1
        dic[front] += 1
        players[idx],players[idx-1] = players[idx-1],players[idx]

    return players