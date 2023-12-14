import heapq
import math
class BestRoute:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in range(1, n + 1)}
        
    def add_road(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        self.graph[node_b].append((node_a, weight))
        
    def find_distances(self, start_node, end_node):
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
                    
        return distances[end_node]

    def find_route(self, a, b):
        path = self.find_distances(a, b)
        infinite = math.isinf(path)
        if infinite == True:
            return -1
        else:
            return path

# add_road: lisää tien kaupungista a kaupunkiin b, jonka pituus on x
# best_route: palauttaa lyhimmän reitin pituuden kaupungista a kaupunkiin b (jos mitään reittiä ei ole olemassa, metodin tulee palauttaa -1)
   

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3)) # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3)) # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3)) # 3