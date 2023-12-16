class Ball:
    def __init__(self,n):
        self.last = 2*n+1
        self.n = n
        self.nodes = range(0, 2*n + 2)
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0
        for i in self.nodes:
            if i in range(1, n+1):
                self.graph[(0, i)] = 1
            if i in range(n+1, 2*n+1):
                self.graph[(i, self.last)] = 1
       # for i in range(1, n+1):
       #     for j in range(n+1, 2*n+1):
       #         self.graph[(i, j)] = 0

    def add_pair(self, node_a, node_b, capacity=1):
        node_b = node_b + self.n
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def calculate(self):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(0, self.last, float("inf"))
            if add == 0:
                break
            total += add

        return total

if __name__ == "__main__":
    b = Ball(5)
    b.add_pair(4,3)
    print(b.calculate())
    b.add_pair(4,1)
    print(b.calculate())
    b.add_pair(2,2)
    print(b.calculate())
    b.add_pair(5,3)
    print(b.calculate())
    print(b.calculate())
    print(b.calculate())
    b.add_pair(1,1)
    print(b.calculate())
    print([node for node in b.graph if b.graph[node] == 1])