"""
push_first(x): lisää luku x listan alkuun
push_last(x): lisää luku x listan loppuun
pop_first(): palauta ja poista alkio listan alusta
pop_last(): palauta ja poista alkio listan lopusta
flip(): käännä listan sisältö
"""
from collections import deque

class FlipList:
    def __init__(self):
        self.numbers = deque()
        self.turned = False

    def push_first(self,x):
        if self.turned == False:
            self.numbers.appendleft(x)
        else:
            self.numbers.append(x)

    def push_last(self,x):
        if self.turned == False:
            self.numbers.append(x)
        else:
            self.numbers.appendleft(x)

    def pop_first(self):
        if self.turned == False:
            return self.numbers.popleft()
        else:
            return self.numbers.pop()

    def pop_last(self):
        if self.turned == False:
            return self.numbers.pop()
        else:
            return self.numbers.popleft()

    def flip(self):
        self.turned = not self.turned

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first()) # 1
    f.flip()
    print(f.pop_first()) # 3