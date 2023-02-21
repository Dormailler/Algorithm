def solution(cacheSize, cities):
    cache = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        i = i.upper()
        if i in cache:
            cache.append(cache.pop(cache.index(i)))
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(i)
            answer += 5 
    return answer