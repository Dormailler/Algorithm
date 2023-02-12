def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = str(bin(arr1[i])[2:])
        arr2[i] = str(bin(arr2[i])[2:])
    for i in range(n): 
        while len(arr1[i]) != n :
            arr1[i] = "0" + arr1[i]
        while len(arr2[i]) != n :
            arr2[i] = "0" + arr2[i]
        temp = [' '] * n
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp[j] = '#'
        arr1[i] = ''.join(temp)
    return arr1