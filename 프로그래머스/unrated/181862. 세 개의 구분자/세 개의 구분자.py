def solution(myStr):
    answer = []
    spr = ["a","b","c"]
    st = ""
    for i in myStr:
        if i not in spr:
            st += i
        else:
            if st == "" :
                continue
            answer.append(st)
            st = ""
    if st != "":
        answer.append(st)
    if answer == []:
        answer.append("EMPTY")
    return answer