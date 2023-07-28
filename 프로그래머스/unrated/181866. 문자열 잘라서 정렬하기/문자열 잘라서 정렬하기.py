def solution(myString):
    s = myString.split("x")
    while "" in s:
        s.remove("")
    return sorted(s)