def solution(cacheSize, cities):
    cache = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        i = i.upper()
        if len(cache) < cacheSize:
            if i not in cache:
                cache.append(i)
                answer += 5
            else:
                cache.append(cache.pop(cache.index(i)))
                answer +=1
            continue
        if i.upper() in cache:
            cache.append(cache.pop(cache.index(i)))
            answer += 1
        else:
            cache.pop(0)
            cache.append(i)
            answer += 5 
    return answer