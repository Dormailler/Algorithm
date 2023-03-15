from collections import deque
def solution(queu1, queu2):
    answer = 0
    q1 = deque(queu1)
    q2 = deque(queu2)
    queue1 = deque(queu1)
    queue2 = deque(queu2)
    total = (sum(queue1) + sum(queue2))
    m = max(max(queu1),max(queu2))
    if total % 2 != 0:
        return -1
    else:
        total //= 2  
    total1 = sum(queue1)
    t1 = total1
    total2 = sum(queue2)
    t2 = total2
    l = len(queue1)
    i = 0
    while total1 != total2 :
        i += 1
        if i > l*3:
            return -1
        if total1 == total2:
            break
        if(total1 > total):
            total1 -= queue1[0]
            total2 += queue1[0]
            queue2.append(queue1.popleft())
        else:
            total1 += queue2[0]
            total2 -= queue2[0]
            queue1.append(queue2.popleft())
        answer += 1
        if total1 <= 0 or total2 <= 0 or queue1 == q1 :
            return -1
    return answer