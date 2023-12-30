class Median:
    def __init__(self):
        pass

    def add(self, x):
        pass

    def median(self):
        pass

if __name__ == "__main__":
    m = Median()
    m.add(1)
    print(m.median()) # 1
    m.add(2)
    print(m.median()) # 1
    m.add(1)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 2