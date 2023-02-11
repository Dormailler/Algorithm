def solution(s):
    answer = ''
    index = 0
    s = list(s)
    index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            index = 0
            continue
        if index % 2 == 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        index += 1
    return ''.join(s)