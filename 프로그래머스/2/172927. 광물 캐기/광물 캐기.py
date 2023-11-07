def solution(picks, minerals):
    d,ir,s = picks[0],picks[1],picks[2]
    i = 0
    answer = 0
    m = []
    while i < len(minerals)+1:
        if i >= (d+ir+s) * 5:
            break
        num = 0
        k = 0
        for j in range(i,min(i+5,len(minerals))):
            if minerals[j] == "diamond":
                num += 25
            elif minerals[j] == "iron":
                num += 5
            else:
                num += 1
        m.append([num,minerals[i:min(i+5,len(minerals))]])
        i += 5
    m.sort(key = lambda x : x[0],reverse=True)
    for n,mineral in m:
        if d > 0:
            answer += len(mineral)
            d -= 1
        elif ir > 0:
            for mi in mineral:
                if mi == "diamond":
                    answer += 5
                else:
                    answer += 1
            ir -= 1
        elif s > 0:
            for mi in mineral:
                if mi == "diamond":
                    answer += 25
                elif mi == "iron":
                    answer += 5
                else:
                    answer += 1
            s -= 1

    return answer