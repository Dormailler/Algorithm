def solution(points, routes):
    answer = 0
    l = len(routes)
    direction = []
    for r in routes:
        d = []
        for j in r:
            d.append(points[j-1])
        direction.append(d)
    locations = []

    for direct in direction:
        location = []
        for i in range(len(direct)-1):
            now = direct[i].copy()
            target = direct[i+1].copy()
            if i == 0:
                location.append(now.copy())

            while now != target:
                if target[0] > now[0]:
                    now[0] += 1
                elif target[0] < now[0]:
                    now[0] -= 1
                elif target[1] > now[1]:
                    now[1] += 1
                elif target[1] < now[1]:
                    now[1] -= 1
                
                location.append(now.copy()) 
        locations.append(location)   
    m = 0 
    for loc in locations:
        if len(loc) > m :
            m = len(loc)
    for i in range(len(locations)):
        while len(locations[i]) < m:
            locations[i].append([0,0])

    for i in range(m):
        set1 = set()
        set2 = set()
        for loc in locations:
            key = tuple(loc[i])
            if key in set1:
                set2.add(key)
            set1.add(key)
        set2.discard((0,0))

        answer += len(set2)
    return answer