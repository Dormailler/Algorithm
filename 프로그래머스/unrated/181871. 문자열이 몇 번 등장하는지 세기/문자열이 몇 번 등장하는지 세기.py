def solution(myString, pat):
    s = ""
    num = 0
    for i in range(len(myString)):
        s += myString[i]
        if len(s) < len(pat):
            continue
        if s[-len(pat):] == pat:
            num += 1
            s = s[-len(pat)+1:]
    return num