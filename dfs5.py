
def square(grid):
    x=[0]
    count=0
    def dfs(i,j):
        nonlocal x,count
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j]==0:
            return 0
        grid[i][j]=0
        count+=1 
        if i>=n-1 or j>=m-1:
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        else:
            if grid[i+1][j]==1 or grid[i-1][j]==1 or grid[i][j+1]==1 or grid[i][j-1]==1:
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
            else:
                x.append(count)
                count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                dfs(i,j)
    return x

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,0,0,0,1,1,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0]]

print(max(square(grid)))