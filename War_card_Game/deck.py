from card import Card

class Deck:

    def __init__(self):
        self.L=[]

    def add(self, rank, suit):
        c = Card(rank, suit)
        self.L.append(c.image())

    def names(self):
        print(len(self.L))

    def remove(self):
        del(self.L[-1])

    def look(self):
        print(self.L[-1])