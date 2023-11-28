def solution(cap, n, deliveries, pickups):
    answer = 0
    idx = 0

    while any(deliveries) or any(pickups):
        n1 = 0
        n2 = 0
        idx = 0

        for i in range(n - 1, -1, -1):
            if deliveries[i] > 0:
                if n1 != cap:
                    b_n1 = n1
                    n1 = min(cap, n1 + deliveries[i])
                    deliveries[i] -= n1 - b_n1
                else:
                    break

        for i in range(n - 1, -1, -1):
            if pickups[i] > 0:
                if n2 != cap:
                    b_n2 = n2
                    n2 = min(cap, n2 + pickups[i])
                    pickups[i] -= n2 - b_n2
                else:
                    break

        if n1 == cap or n2 == cap:
            idx += 1
            n = idx

        answer += idx * 2

    return answer