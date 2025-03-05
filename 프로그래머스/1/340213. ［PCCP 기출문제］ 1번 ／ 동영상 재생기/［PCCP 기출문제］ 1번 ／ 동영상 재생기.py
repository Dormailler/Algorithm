def solution(video_len, pos, op_start, op_end, commands):
    answer = pos
    for command in commands:
        if command == "next":
            if op_start <= answer <= op_end:
                answer = op_end
            minute = int(answer[3:]) + 10
            if minute > 59:
                minute -= 60
                hour = int(answer[:2]) + 1
                answer = str(hour).zfill(2) + ":" + str(minute).zfill(2)
            else:
                answer = answer[:3] + str(minute).zfill(2)
            
        elif command == "prev":
            if op_start <= answer <= op_end:
                answer = op_end
            minute = int(answer[3:]) - 10
            if minute < 0:
                minute += 60
                hour = int(answer[:2]) - 1
                if hour < 0:
                    answer = "00:00"
                else:
                    answer = str(hour).zfill(2) + ":" + str(minute).zfill(2)
            else:
                answer = answer[:3] + str(minute).zfill(2)
        if answer > video_len:
            answer = video_len
        if op_start <= answer <= op_end:
            answer = op_end
    return answer