def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i == 'left' and abs(answer[0] - 1) <= (board[0]-1)//2 :
            answer[0] -= 1
        elif i == 'right' and answer[0] + 1 <= (board[0]-1)//2:
            answer[0] += 1
        elif i == 'up' and answer[1] + 1 <= (board[1]-1)//2 :
            answer[1] += 1
        elif i == 'down' and abs(answer[1] - 1) <= (board[1]-1)//2:
                answer[1] -= 1
    return answer