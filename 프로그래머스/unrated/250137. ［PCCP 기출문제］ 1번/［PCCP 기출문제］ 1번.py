def solution(bandage, health, attacks):
    time = 0
    max_health = health
    cont = 0
    for a in attacks:
        for i in range(time,a[0]-1):
            if health == max_health:
                cont += 1
            else:
                health = min(max_health,health+bandage[1])
                cont += 1
            if cont == bandage[0]:
                cont = 0
                health = min(max_health,health+bandage[2])

        cont = 0
        time = a[0]
        health -= a[1]

        if health <= 0:
            return -1
    
    return health