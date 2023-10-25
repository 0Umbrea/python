def total(rooms):
    visited=set()
    def dfs(x):
        nonlocal visited
        visited.add(x)
        for i in rooms[x]:
            if i not in visited:
                dfs(i)
    dfs(0)
    return(len(visited)==len(rooms))

rooms = [[1,3],[3,0,1],[2],[0]]
print(total(rooms))