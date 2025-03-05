def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        day = startday
        gtime = schedules[i] + 10
        if gtime % 100 > 59:
            gtime += 40
        rtime = timelogs[i]
        for t in rtime:
            if t > gtime and day not in (6,7):
                break
            day += 1
            if day > 7:
                day -= 7
        else:
            answer += 1
    return answer