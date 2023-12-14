"""
add_road lisää tien kahden kaupungin välille
count ilmoittaa komponenttien määrän
"""
class UnionFind:
    def __init__(self, n):
        self.link = {node: None for node in range(1, n + 1)}
        self.size = {node: 1 for node in range(1, n + 1)}
            
    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
 
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]  

class Components:
    def __init__(self, n):
        self.n = n
        self.cities = UnionFind(n)

    def add_road(self, a, b):
        self.cities.union(a,b)

    def count(self):
        numbers = set()
        for i in range(1,self.n+1):
            numbers.add(self.cities.find(i))
        return len(numbers)

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count()) # 3
    c.add_road(2, 3)
    print(c.count()) # 3
    c.add_road(4, 5)
    print(c.count()) # 2