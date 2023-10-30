class solution:
    def topologicalsortingDFS(self,graph:dict):
        onstack=set()
        visited=set()
        hascycle=True
        order=[]
        def dfs(u):
            nonlocal hascycle
            if u in onstack:
                hascycle=False
            if u in visited or hascycle:
                return
            visited.add(u)
            onstack.add(u)
            if len(graph)>1:
                for i in graph[u]:
                    dfs(i)
            order.append(u)
            onstack.remove(u)
        for u in graph:
            if u not in visited:
                dfs(u)
        return hascycle
    def find(self,numcourses,prerequisites):
        graph=dict()
        for i in range(numcourses):
            graph[i]=[]
        for u,v in prerequisites:
            graph[v].append(u)
        return self.topologicalsortingDFS(graph)


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(solution().find(numCourses,prerequisites))