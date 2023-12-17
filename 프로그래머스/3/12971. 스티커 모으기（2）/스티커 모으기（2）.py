def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    sticker1 = sticker[:-1]
    sticker2 = sticker[1:]
    l = len(sticker1)
    i = 1
    while i < l:
        if i == 1:
            sticker1[i] = max(sticker1[i-1],sticker1[i])
            sticker2[i] = max(sticker2[i-1],sticker2[i])
            i += 1
            continue
        sticker1[i] = max(sticker1[i-1],(sticker1[i-2] + sticker1[i]))
        sticker2[i] = max(sticker2[i-1],(sticker2[i-2] + sticker2[i]))
        i += 1
    return max(max(sticker1),max(sticker2))