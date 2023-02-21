def solution(s):
    answer = []
    stack = []
    arr = []
    i = 0
    while i < len(s):
        num = ""
        while s[i].isdigit():
            num += s[i]
            i += 1
        if num != "":
            arr.append(num)
        if s[i] == '}' and arr != []:
            stack.append(arr)
            arr = []
        i += 1
    stack.sort(key=lambda x:len(x))
    for i in stack:
        for n in i:
            if int(n) not in answer:
                answer.append(int(n))
    return answer