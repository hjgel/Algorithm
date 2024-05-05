def solution(board):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                for i in range(8):
                    nx = x + dx[i] 
                    ny = y + dy[i]
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board) and board[nx][ny] == 0:
                        answer += 1
                        board[nx][ny] = 2
    return answer
                       
print(solution([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0]]))
