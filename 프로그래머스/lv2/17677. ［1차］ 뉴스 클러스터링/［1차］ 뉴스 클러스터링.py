def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    li1 = [str1[i] + str1[i+1] for i in range(len(str1)-1) 
          if str1[i].isalpha() and str1[i+1].isalpha()]
    li2 = [str2[i] + str2[i+1] for i in range(len(str2)-1) 
          if str2[i].isalpha() and str2[i+1].isalpha()]
    dic1 = {}
    dic2 = {}
    for i in li1:
        if i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] +=1
    for i in li2:
        if i not in dic2:
            dic2[i] = 1
        else:
            dic2[i] +=1
    go = 0
    hap = 0
    for i in dic1:
        if i in dic2:
            go += min(dic1[i],dic2[i])
            hap += max(dic1[i],dic2[i])
            dic2[i] = 0
        else:
            hap += dic1[i]
    for i in dic2:
        hap += dic2[i]
    if go == 0 and hap != 0:
        return 0
    if go == 0 or hap == 0:
        return 65536
    
    return go/hap*65536//1