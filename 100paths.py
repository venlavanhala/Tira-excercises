

class CountPaths:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in self.nodes}
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        
    def count_from(self, node):
        if node in self.result:
            return self.result[node]
        
        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)
        
        self.result[node] = path_count
        return path_count
        
    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)

g = CountPaths(101)

for i in range(2,102):
    g.add_edge(1,i)
    g.add_edge(i,103)


#print(g.graph)
print(g.count_paths(1,103))
"""
i = 1
while g.count_paths(1, 101) <= 100 and i<98:
    g.add_edge(i, i+1)
    if g.count_paths(1, 101) == 100:
        break
"""