def solution(board):
    num = 0
    a = [[0]*len(board) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                a[i][j] = 1
                if i-1 >= 0:
                    a[i-1][j] = 1
                    if j-1 >= 0:
                        a[i-1][j-1] = 1
                    if j+1 < len(board):
                        a[i-1][j+1] = 1
                if j-1 >= 0:
                    a[i][j-1] = 1
                if i+1 < len(board):
                    a[i+1][j] = 1
                    if j-1 >= 0:
                        a[i+1][j-1] = 1
                    if j+1 <len(board):
                        a[i+1][j+1] = 1
                if j+1 < len(board):
                    a[i][j+1] = 1
    for i in range(len(board)):
        num += a[i].count(0)
    return num