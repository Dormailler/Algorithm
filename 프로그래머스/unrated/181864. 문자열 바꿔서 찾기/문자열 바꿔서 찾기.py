def solution(myString, pat):
    myString = myString.replace("A","b")
    myString = myString.replace("B","a").upper()
    if pat in myString:
        return 1
    return 0