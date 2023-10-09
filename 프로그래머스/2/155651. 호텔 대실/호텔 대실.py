def solution(book_time):
    room = []
    book_time.sort(key=lambda x:x[0])
    for time in book_time:
        hour = time[1][0:2]
        p_hour = str(int(hour)+1)
        if len(p_hour) == 1:
            p_hour = "0" + p_hour
        minute = int(time[1][3:5])
        p_minute = str(minute+9)
        if len(p_minute) == 1:
            p_minute = "0" + p_minute
        if room == []:
            if minute+9 > 59:
                room.append(p_hour+":0"+str(minute-51))
            else:
                room.append(hour+":"+p_minute)
        else:
            for i in range(len(room)):
                if room[i] < time[0]:
                    if minute+9 > 59:
                        room[i] = p_hour+":0"+str(minute-51)
                    else:
                        room[i] = hour+":"+p_minute
                    break
            else:
                if int(time[1][3:5])+9 > 59:
                    room.append(p_hour+":0"+str(minute-51))
                else:
                    room.append(hour+":"+p_minute)
    return len(room)