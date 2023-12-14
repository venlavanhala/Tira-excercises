"""
Voit joka askeleella liikkua ylös, alas, vasemmalle tai oikealle.
Et saa kuitenkaan mennä ruudukon ulkopuolelle. Valitsemasi reitin hinta on 
lukujen summa reitillä. Mikä on pienin mahdollinen reitin hinta?
"""

import heapq

class Dijkstra:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in range(1, n + 1)}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        self.graph[node_b].append((node_a, weight))
        
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

def count(m):
    r = Dijkstra(len(m)*len(m[0]))
    for i in range(0, len(m)-1):
        for j in range(0, len(m[0])):
            print(m[i][j], m[i+1][j])
            r.add_edge((i,j), (i,j+1), m[i][j])

    for i in range(0, len(m)):
        for j in range(0, len(m[0])-1):
            print(m[i][j], m[i][j+1])

if __name__ == "__main__":
    r = [[2, 1, 4, 8],
         [3, 8, 7, 2],
         [9, 5, 1, 2]]
    print(count(r)) # 17