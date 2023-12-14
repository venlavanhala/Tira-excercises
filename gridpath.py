"""
Voit joka askeleella liikkua ylös, alas, vasemmalle tai oikealle.
Et saa kuitenkaan mennä ruudukon ulkopuolelle. Valitsemasi reitin hinta on 
lukujen summa reitillä. Mikä on pienin mahdollinen reitin hinta?
"""

import heapq

class Dijkstra:
    def __init__(self, n):
        self.nodes = range(0, n)
        self.graph = {node: [] for node in range(0, n)}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        #self.graph[node_b].append((node_a, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        queue = []
        heapq.heappush(queue, (0, start_node))
        
        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)
                    
        return distances

def count(matrix):
    nodes = range(len(matrix) * len(matrix[0]))
    lenght = len(nodes)
    places = {}
    inde = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            places[inde]=matrix[i][j]
            inde += 1

    g = Dijkstra(lenght)
    for node in places.keys():
        for node2 in places.keys():
            if node == node2 + 1 or node == node2 - 1:
                g.add_edge(node, node2, places[node])
            if node == node2 + len(matrix[0]) or node == node2 - len(matrix[0]):
                 g.add_edge(node, node2, places[node])
    distance = g.find_distances(0)

    return g.graph
    return distance[max(nodes)] + matrix[-1][-1]

if __name__ == "__main__":
    r = [[4, 3, 6, 10, 8, 10, 5, 4], [9, 2, 9, 10, 10, 1, 2, 7]]
    print(count(r)) # 48