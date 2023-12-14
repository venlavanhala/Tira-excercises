import heapq

class Dijkstra:
    def __init__(self, n):
        self.nodes = self.nodes = range(0, n)
        self.graph = {node: [] for node in range(0, n)}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        
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

# Kun olet alkion x kohdalla, saat hypätä x askelta vasemmalle tai oikealle. 
# Et saa kuitenkaan tehdä hyppyä, joka veisi listan ulkopuolelle. Sinun tulee päästä listan loppuun niin, 
# että hyppyjen kokonaismatka on mahdollisimman pieni.   

def calculate(path):
    lst = Dijkstra(len(path))
    for i in range(0,len(path)):
        for j in range(0, len(path)):
            if abs(j-i) == path[j]:
                lst.add_edge(j, i, path[j])
                #print(f"added j, i: {j, i}")
    distance = lst.find_distances(0)
   # print(distance)
    if distance[len(path)-1] != float("inf"):
        return distance[len(path)-1]
    else:
        return -1


if __name__ == "__main__":
    print(calculate([1, 1, 1, 1])) # 3
    print(calculate([3, 2, 1])) # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5])) # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32