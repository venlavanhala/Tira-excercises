
class AllPaths:
    def __init__(self, n):
        self.n = n
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in self.nodes}
        self.all = 0
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        
    def count_from(self, node):
        for next_node in self.graph[node]:
            if self.count_from(next_node) != None:
                self.all += self.count_from(next_node)
        return self.all
        
    def count(self):
        self.result = {self.n: 1}
        self.count_from(1)
        return self.all

if __name__ == "__main__":
    a = AllPaths(4)
    a.add_edge(1, 2)
    a.add_edge(1, 3)
    a.add_edge(2, 4)
    a.add_edge(3, 4)
    print(a.count()) # 10
    a.add_edge(2, 3)
    print(a.count()) # 14