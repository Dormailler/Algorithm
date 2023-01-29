def solution(my_string):
    i = 0
    a = []
    while i < len(my_string):
        s = ''
        c = 0
        while my_string[i].isdigit():
            s += my_string[i]
            c = 1
            i += 1
            if i >= len(my_string):
                break
        if c == 1:
            i -= 1
        if s != '':
            a.append(s)
        i += 1
    return sum(list(map(int,a)))