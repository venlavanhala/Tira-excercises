# add_course lisää annetun nimisen kurssin
# add_requisite lisää esitietovaatimuksen
# find_order etsii jonkin tavan suorittaa kurssit ja palauttaa järjestyksen 
   #listana (jos mitään tapaa ei ole, metodi palauttaa None)


class CoursePlan:
    def __init__(self):
        self.nodes = []
        self.graph = {}

    def add_course(self, course):
        self.nodes.append(course)
        self.graph[course] = []

    def add_requisite(self, course1, course2):
        self.graph[course1].append(course2)

    def visit(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return

        self.state[node] = 1
        for next_node in self.graph[node]:
            self.visit(next_node)

        self.state[node] = 2
        self.order.append(node)
        
    def find_order(self):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False
        
        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)
                
        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]
    c.add_requisite("Tira", "Tira")
    print(c.find_order()) # None