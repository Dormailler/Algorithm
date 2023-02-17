def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i].upper()
            continue
        if s[i] == " ":
            continue
        if s[i-1] == " " and s[i] != " ":
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    return ''.join(s)