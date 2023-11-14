def solution(plans):
    plans.sort(key=lambda x:x[1])
    answer = []
    remain = []
    work = []
    time = ""
    for i in plans:
        name = i[0]
        start = i[1]
        playtime = int(i[2])
        now = int(start[0:2]) * 60 + int(start[3:]) 
        time = now
        af_time = now + playtime
        if work == []:
            work.append([name,playtime,af_time])
        else:
            b_name,b_playtime,b_af_time = work.pop()
            if b_af_time > time:
                remain.append([b_name,b_af_time-time])
            else:
                answer.append(b_name)
                a_time = b_af_time
                while remain != []:
                    b_name,b_remain_time= remain.pop()
                    if a_time + b_remain_time > time:
                        remain.append([b_name,a_time + b_remain_time - time])
                        break
                    else:
                        answer.append(b_name)
                        a_time = a_time + b_remain_time
            work.append([name,playtime,af_time])
    answer.append(work[0][0])
    while remain != []:
        answer.append(remain.pop()[0])
    return answer