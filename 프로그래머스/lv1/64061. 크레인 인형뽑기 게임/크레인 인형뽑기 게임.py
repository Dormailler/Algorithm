def solution(board, moves):
    box = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                break
        if  board[j][i-1] == 0:
            continue
        if box != []:
            if board[j][i-1] == box[-1]:
                board[j][i-1] = 0
                box.pop()
                answer += 2
            else:
                box.append(board[j][i-1])
                board[j][i-1] = 0
        else:
            box.append(board[j][i-1])
            board[j][i-1] = 0
    print(box)
    return answer