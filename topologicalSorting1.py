import collections

class solution:
    def topologicalsorting(self,graph:dict):
        indegrees={i:0 for i in graph}
        order=[]
        for u in graph:
            for v in graph[u]:
                indegrees[v]+=1
        s=collections.deque([u for u in indegrees if indegrees[u]==0])
        while s:
            u=s.pop()
            order.append(u)
            for v in graph[u]:
                indegrees[v]-=1
                if indegrees[v]==0:
                    s.append(v)
        if len(indegrees)!=len(order):
            return []
        return order
    def find(self,numcoures,prerequisites):
        graph=dict()
        for i in range(numcoures):
            graph[i]=[]
        for u,v in prerequisites:
            graph[v].append(u)
        return self.topologicalsorting(graph)

numCourses = 4 
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(solution().find(numCourses,prerequisites))
