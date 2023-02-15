def solution(numbers, hand):
    answer = ''
    lx = 1
    ly = 4
    rx = 3
    ry = 4
    left = {1:1,4:2,7:3}
    right = {3:1,6:2,9:3}
    middle = {2:1,5:2,8:3,0:4}
    for i in numbers:
        if i in left:
            answer += 'L'
            lx = 1
            ly = left[i]
        elif i in right:
            answer += 'R'
            rx = 3
            ry = right[i]
        else:
            if abs(lx-2)+abs(ly-middle[i]) == abs(rx-2)+abs(ry-middle[i]):
                if hand == 'left':
                    answer += 'L'
                    lx = 2
                    ly = middle[i]
                else:
                    answer += 'R'
                    rx = 2
                    ry = middle[i]
            elif abs(lx-2)+abs(ly-middle[i]) < abs(rx-2)+abs(ry-middle[i]):
                answer += 'L'
                lx = 2
                ly = middle[i]
            else:
                answer += 'R'
                rx = 2
                ry = middle[i]
    return answer