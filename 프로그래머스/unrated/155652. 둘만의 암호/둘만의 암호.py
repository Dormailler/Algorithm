def solution(s, skip, index):
    s = list(s)
    for i in range(len(s)):
        for j in range(index):
            s[i] = chr(ord(s[i])+1)
            if ord(s[i]) >= 123:
                s[i] = chr(ord(s[i]) - 26)
            while s[i] in skip:
                s[i] = chr(ord(s[i])+1)
                if ord(s[i]) >= 123:
                    s[i] = chr(ord(s[i]) - 26)
    return ''.join(s)