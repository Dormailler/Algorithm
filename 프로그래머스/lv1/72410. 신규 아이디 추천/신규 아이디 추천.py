def solution(new_id):
    anser = ''
    new_id = new_id.lower()
    new_id = list(new_id)
    n = "abcdefghijklmnopqrstuvwxyz1234567890-_."
    for i in range(len(new_id)):
        if new_id[i] not in n:
            new_id[i] = ""
    new_id = list(''.join(new_id))
    for i in range(len(new_id)-1):
        if new_id[i] == '.' and new_id[i+1] == '.':
            new_id[i] = ''
    new_id = list(''.join(new_id))
    for i in range(len(new_id)):
        if new_id[i] == "":
            continue
        else:
            if new_id[i] == '.':
                new_id.pop(i)
            break
    for i in range(len(new_id)-1,-1,-1):
        if new_id[i] == "":
            continue
        else:
            if new_id[i] == '.':
                new_id.pop(i)
            break
    new_id = ''.join(new_id)
    if new_id == "":
        new_id = "a"
    new_id = list(new_id)
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id.pop()
    if len(new_id) <= 2:
        st = new_id[-1]
        while len(new_id) != 3:
            new_id.append(st)
    return ''.join(new_id)