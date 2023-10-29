
def girth(gird):
    count=5
    visited=list()
    add=list()
    def bfs(i,j):
        nonlocal count,visited,add
        m=len(gird)
        n=len(gird[0])
        if i<0 and i>m and j<0 and j>m and gird[i][j]==0:
            return 0
        count-=1
        if len(visited)<2:
            visited.append(i)
            visited.append(j)
        if gird[i][j]==1 and i<visited[0]+1 and i>visited[0]-1 and j<visited[1]+1 and j>visited[1]-1:
            bfs(i-1,j)
            bfs(i+1,j)
            bfs(i,j-1)
            bfs(i,j+1)
            visited=[]
        add.append(count)
        count=5
    for i in range(len(gird)):
        for j in range(len(gird[0])):
            bfs(i,j)
    x=sum(add)
    return add

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(girth(grid))