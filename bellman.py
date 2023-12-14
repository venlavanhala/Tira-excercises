
#Verkossa on solmut 1,2,...N ja N=5000.
#Aloitussolmu on solmu 1.
#Solmusta a on kaari solmuun b, jos a<b ja b-a<10.
#Jokaisen kaaren paino on satunnainen kokonaisluku välillä 1...1000
#Kaaret ovat satunnaisessa järjestyksessä kaarilistassa.

import random
import time
start = time.time()

class BellmanFord:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        for _ in range(len(self.nodes) - 1):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    
        return distances
    
bellman = BellmanFord(5000)
for a in range(1,5001):
    for b in range(1,5001):
        if a<b and b-a<20:
            weight = random.randint(1,1000)
            bellman.add_edge(a, b, weight)
print(bellman.find_distances(1))

end = time.time()

print(end-start)