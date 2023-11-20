def solution(board):
    o = 0
    x = 0
    ko = 0
    kx = 0
    dic = {0:"",1:"",2:""}
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        ko += 1
    elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        kx += 1
    for i in board:
        if i == "OOO":
            ko += 1
        elif i == "XXX":
            kx += 1
        for j in range(len(i)):
            if i[j] == "X":
                dic[j] += "X"
                x += 1
            elif i[j] == "O":
                dic[j] += "O"
                o += 1
    for i in dic:
        if dic[i] == "OOO":
            ko += 1
        elif dic[i] == "XXX":
            kx += 1

    if abs(x-o) > 1 or (ko>0 and kx >0) or x > o or kx > 1 or (kx > 0 and o > x) or (ko > 0 and x == o):
        return 0
    
    return 1