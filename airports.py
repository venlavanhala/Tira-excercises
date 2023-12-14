# add_link lisää yksisuuntaisen yhteyden kentältä a kentälle b
# check ilmoittaa, voiko jokaiselta kentältä saavuttaa kaikki muut kentät


class Airports:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in self.nodes}
        self.reverse = {node: [] for node in self.nodes}
        
    def add_link(self, a, b):
        self.graph[a].append(b)
        self.reverse[b].append(a)
        
    def visit(self, node, phase):
        if node in self.visited:
            return
        self.visited.add(node)

        if phase == 1:
            graph = self.graph
        if phase == 2:
            graph = self.reverse
        
        for next_node in graph[node]:
            self.visit(next_node, phase)

        if phase == 1:
            self.order.append(node)
        
    def check(self):
        self.visited = set()
        self.order = []
        
        for node in self.nodes:
            self.visit(node, 1)
                
        self.order.reverse()
        self.visited.clear()

        count = 0
        for node in self.order:
            if node not in self.visited:
                count += 1
                self.visit(node, 2)
                
        return count==1
    
if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check()) # False
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check()) # False
    a.add_link(5, 1)
    print(a.check()) # True