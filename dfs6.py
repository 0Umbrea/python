def back(board):
    def dfs(i,j):
        m=len(board)
        n=len(board[0])
        board[i][j]='X'
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == 'X':
            return 0
        if i>0 and i<m-1 and j>0 and j<n-1:
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            dfs(i,j)
    return board


board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
print(back(board))