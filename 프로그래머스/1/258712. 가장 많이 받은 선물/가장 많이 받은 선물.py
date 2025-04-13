def solution(friends, gifts):
    answer = 0
    length = len(friends)
    arr = [0 for i in range(length)]
    num = [0 for i in range(length)]
    dic = {}
    
    for i in friends:
        for j in friends:
            if i == j:
                continue
            dic[i + " " + j] = 0
            dic[j + " " + i] = 0
    
    for gift in gifts:
        if gift in dic:
            dic[gift] += 1
        a,b = gift.split() 
        arr[friends.index(a)] += 1
        arr[friends.index(b)] -= 1
    for i in range(length):
        for j in range(1,length - i):
            if dic[friends[i] + " " + friends[i+j]] > dic[friends[i+j] + " " + friends[i]]:
                num[i] += 1
            elif dic[friends[i] + " " + friends[i+j]] < dic[friends[i+j] + " " + friends[i]]:
                num[i+j] += 1
            elif arr[i] > arr[i+j]:
                num[i] += 1
            elif arr[i] < arr[i+j]: 
                num[i+j] += 1
    return max(num)