def solution(my_string):
    s = my_string.split()
    for i in range(len(s)):
        if s[i] == '+':
            s[i+1] = int(s[i-1]) + int(s[i+1])
        elif s[i] == '-':
            s[i+1] = int(s[i-1]) - int(s[i+1])
    return s[-1]