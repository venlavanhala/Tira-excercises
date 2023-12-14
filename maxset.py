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

#merge yhdistää joukot, joissa on luvut a ja b (jos ne ovat eri joukoissa)
#get_max ilmoittaa suurimman joukon koon

class MaxSet:
    def __init__(self, n):
        self.set = UnionFind(n)
        self.biggest = 1

    def merge(self, a, b):
        self.set.union(a,b)
        a = self.set.find(a)
        size_a = self.set.size[a]
        #print(size_a)
        if size_a > self.biggest:
            self.biggest = size_a

    def get_max(self):
        return self.biggest

if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max()) # 3
    m.merge(1, 5)
    print(m.get_max()) # 5
