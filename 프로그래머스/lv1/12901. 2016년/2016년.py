def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month = [0,0,31,60,91,121,152,182,213,244,274,305,335]
    d = (month[a] + b + 4) % 7 
    return day[d]

