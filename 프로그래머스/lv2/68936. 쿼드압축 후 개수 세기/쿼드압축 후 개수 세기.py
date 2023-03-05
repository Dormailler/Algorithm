def div(array,st):
    num = 0
    l = len(array)
    if l == 1:
        if array[0] == 1:
            st[1] += 1
        else:
            st[0] += 1
        return st
    arr1 = [[array[i][j] for j in range(l//2)] for i in range(l//2)]
    arr2 = [[array[i][j] for j in range(l//2)] for i in range(l//2,l)]
    arr3 = [[array[i][j] for j in range(l//2,l)] for i in range(l//2)]
    arr4 = [[array[i][j] for j in range(l//2,l)] for i in range(l//2,l)]

    if all(sum(arr1[i]) == 0 for i in range(l//2)):
        st[0] += 1
    elif all(sum(arr1[i]) == l//2 for i in range(l//2)):
        st[1] += 1
    else:
        st = div(arr1,st)
    if all(sum(arr2[i]) == 0 for i in range(l//2)):
        st[0] += 1
    elif all(sum(arr2[i]) == l//2 for i in range(l//2)):
        st[1] += 1
    else:
        temp_st = div(arr2,st)
    if all(sum(arr3[i]) == 0 for i in range(l//2)):
        st[0] += 1
    elif all(sum(arr3[i]) == l//2 for i in range(l//2)):
        st[1] += 1
    else:
        temp_st = div(arr3,st)
    if all(sum(arr4[i]) == 0 for i in range(l//2)):
        st[0] += 1
    elif all(sum(arr4[i]) == l//2 for i in range(l//2)):
        st[1] += 1
    else:
        temp_st = div(arr4,st)
    return st
        
def solution(arr):
    stack = [0,0]
    if all(sum(arr[i]) == 0 for i in range(len(arr))):
        stack[0] = 1
        return stack
    elif all(sum(arr[i]) == len(arr) for i in range(len(arr))):
        stack[1] = 1
        return stack
    return div(arr,stack)
