def solution(m, musicinfos):
    answer = ''
    c = 0
    mc = 0
    dic = {}
    for music in musicinfos:
        play = music.split(',')
        playmin = (int(play[1][:2]) - int(play[0][:2])) * 60  + int(play[1][3:]) - int(play[0][3:])
        s = ""
        i = 0
        j = 0
        while i != playmin:
            j = j % len(play[3])
            s += play[3][j]
            if j+1 < len(play[3]) and play[3][j+1] == '#':
                s += "#"
                j += 1
            i += 1
            j += 1 
        s = s.replace("C#",'1')
        s = s.replace("D#",'2')
        s = s.replace("F#",'3')
        s = s.replace("G#",'4')
        s = s.replace("A#",'5')
        m = m.replace("C#",'1')
        m = m.replace("D#",'2')
        m = m.replace("F#",'3')
        m = m.replace("G#",'4')
        m = m.replace("A#",'5')
        if m in s:
                c = playmin
                mc = max(mc,c)
                dic[play[2]] = c
    if mc == 0:
        return "(None)"
    else:
        for i in dic:
            if dic[i] == mc:
                return i