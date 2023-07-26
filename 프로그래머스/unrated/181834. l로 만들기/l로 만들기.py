def solution(myString):
    li = list(myString)
    for i in range(len(li)):
        if li[i] < 'l':
            li[i] = 'l'
    return ''.join(li)
        
        
  