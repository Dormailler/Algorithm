def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        for j in range(n):
            s[i] = chr(ord(s[i])+1)
            if ord(s[i]) >= 91 and ord(s[i]) <= 97:
                s[i] = chr(ord(s[i])-26)
            elif ord(s[i]) >= 123:
                s[i] = chr(ord(s[i])-26)
    return ''.join(s)