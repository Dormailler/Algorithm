def solution(cards):
    a = 0
    ans = []
    while a != len(cards):
        visit = [0 for _ in range(len(cards)+1)]
        s = cards[a]
        p1 = 0
        while visit[s] == 0:
            visit[s] = 1
            s = cards[s-1]
            p1 += 1
        for i in range(len(cards)):
            visit2 = visit.copy()
            p2 = 0
            s = i + 1
            if visit2[s] == 1:
                continue
            while visit2[s] == 0:
                visit2[s] = 1
                s = cards[s-1]
                p2 += 1
            ans.append(p1*p2)
        a += 1
        ans.append(p1*p2)
    return max(ans)