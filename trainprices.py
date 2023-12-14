"""
Tehtäväsi on muodostaa hintataulukko, joka näyttää halvimman hinnan jokaisen kaupungin välillä käyttäen junayhteyksiä.
Taulukon tulee muodostua sisäkkäisistä listoista, ja siinä tulee näkyä kaupunkien nimet ja hinnat. Kaupungit tulee järjestää
aakkosjärjestykseen taulukossa. Jos mitään yhteyttä ei ole, taulukossa tulee näkyä hintana -1. Esimerkki taulukosta on alla olevassa
tehtäväpohjassa.
"""
import math

class TrainPrices:
    def __init__(self):
        self.nodes = []
        self.graph = {}

    def add_city(self, name): #lisää uuden kaupungin
        self.nodes.append(name)
        for node in self.nodes:
            distance = 0 if node == name else float("inf")
            self.graph[(node, name)] = distance
            self.graph[(name, node)] = distance

    def add_train(self, city1, city2, price): # lisää junayhteyden kahden kaupungin välille
        self.graph[(city1, city2)] = min(self.graph[(city1, city2)], price)
        self.graph[(city2, city1)] = min(self.graph[(city2, city1)], price)

    def find_prices(self): #find_prices: palauttaa hintataulukon
        distances = self.graph.copy()

        for k in self.nodes:
            for a in self.nodes:
                for b in self.nodes:
                    distance = min(distances[(a, b)],
                                   distances[(a, k)] + 
                                   distances[(k, b)])
                    distances[(a, b)] = distance

        for path in distances:
            if math.isinf(distances[path]) == True:
                distances[path] = -1
            
        nonelist = [None]
        cities = [node for node in self.nodes]
        cities.sort()
        citylist = nonelist + cities

        all = []
        for lst in distances:
            all.append(list(lst)+[distances[lst]])
        numberlist = []
        for city in cities:
            row = [city]
            for city2 in cities:
                row.append(distances[city, city2])
            numberlist.append(row)

        return [citylist] + numberlist

if __name__ == "__main__":
    t = TrainPrices()

    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)

    print(t.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]