def solution(record):
    numdic = {}
    namedic = {}
    stack = []
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            namedic[i[1]] = i[2]
            stack.append(i[1]+"님이 들어왔습니다.")
        elif i[0] == "Leave":
            stack.append(i[1]+"님이 나갔습니다.")
        else:
            namedic[i[1]] = i[2]
    for i in range(len(stack)):
        stack[i] = stack[i].replace(stack[i][:stack[i].index("님")],namedic[stack[i][:stack[i].index("님")]])
    return stack