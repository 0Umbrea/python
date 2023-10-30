import collections

class solution:
    def topologicalsorting(self,graph):
        indegress={i:0 for i in graph}
        order=[]
        for u in graph:
            for v in graph[u]:
                indegress[v]+=1
        s=collections.deque([i for i in indegress if indegress[i]==0])
        while s:
            x=s.pop()
            for u in graph[x]:
                indegress[u]-=1
                if indegress[u]==0:
                    s.append(u)
        for u in graph:
            if indegress[u]==0:
                order.append(u)
        return order
    def find(self,x):
        graph=dict()
        for i in range(len(x)):
            graph[i]=[]
        for u in range(len(x)):
            for v in x[u]:
                graph[v].append(u)
        return self.topologicalsorting(graph)

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(solution().find(graph))
            

        