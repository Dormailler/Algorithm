def solution(dirs):
    dic = {"U":[],"D":[],"L":[],"R":[]}
    loc = [0,0]
    s = []
    answer = 0 
    for i in list(dirs):
        a = 0
        if i == "U" and loc[1] + 1 <= 5:
            if loc not in dic["U"] and [loc[0],loc[1]+1] not in dic["D"]:
                s = loc.copy()
                dic["U"] += [s]
                dic["D"] += [s[0],s[1]+1]
                answer += 1
            loc[1] += 1
        elif i == "D" and loc[1] - 1 >= -5:
            if loc not in dic["D"] and [loc[0],loc[1]-1] not in dic["U"]:
                s = loc.copy()
                dic["D"] += [s]
                dic["U"] += [s[0],s[1]-1]
                answer += 1
            loc[1] -= 1
        elif i == "L" and loc[0] - 1 >= -5:
            if loc not in dic["L"] and [loc[0]-1,loc[1]] not in dic["R"]:
                s = loc.copy()
                dic["L"] += [s]
                dic["R"] += [s[0]-1,s[1]]
                answer += 1
            loc[0] -= 1
        elif i == "R" and loc[0] + 1 <= 5:
            if loc not in dic["R"] and [loc[0]+1,loc[1]] not in dic["L"]:
                s = loc.copy()
                dic["R"] += [s]
                dic["L"] += [s[0]+1,s[1]]
                answer += 1
            loc[0] += 1
    return answer