def solution(user_id, banned_id):
    banned = [[] for _ in range(len(banned_id))]
    arr2 = []
    for b in range(len(banned_id)):
        for user in user_id:
            if len(banned_id[b]) != len(user):
                continue
            for i in range(len(user)):
                if banned_id[b][i] != "*" and banned_id[b][i] != user[i]:
                    break
            else:
                banned[b].append(user)
    def s(i,arr):
        i += 1
        if i >= len(banned):

            arr2.append(arr)
            return
        for j in banned[i]:
            if j not in arr:
                s(i,arr+[j])
    for j in banned[0]:
        s(0,[j])
    for i in range(len(arr2)):
        arr2[i].sort()
        arr2[i] = set(arr2[i])
    arr3 = []
    for i in range(len(arr2)):
        if arr2[i] not in arr3 and len(arr2[i]) == len(banned):
            arr3.append(arr2[i])
    return len(arr3)