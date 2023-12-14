class Planets:
    def __init__(self,n):
        self.n = n
        self.nodes = range(1, n + 1)
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_teleport(self, node_a, node_b, capacity=1):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow=1):
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
            add = self.add_flow(1, self.n, float("inf"))
            if add == 0:
                break
            total += add
        return total

"""
 add_teleport lisää teleportin planeetalta a planeetalle b
calculate ilmoittaa pienimmän poistettavien teleporttien määrän
"""   

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1, 2)
    p.add_teleport(2, 5)
    print(p.calculate()) # 1
    p.add_teleport(1, 5)
    print(p.calculate()) # 2