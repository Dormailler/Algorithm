def solution(arr):
    arr2 = arr.copy()
    x = 0
    while True:
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        if arr2 == arr:
            return x
        else:
            arr2 = arr.copy()
            x += 1
        