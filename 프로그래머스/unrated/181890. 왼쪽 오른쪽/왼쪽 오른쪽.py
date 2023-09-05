def solution(str_list):
    a = []
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return a
        if str_list[i] == "r":
            return str_list[i+1:]
        a.append(str_list[i])
    return []