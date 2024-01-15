class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = rank + suit
        self.weight = 0
        if rank == '2':
            self.weight = 2
        elif rank == '3':
            self.weight = 3
        elif rank == '4':
            self.weight = 4
        elif rank == '5':
            self.weight = 5
        elif rank == '6':
            self.weight = 6
        elif rank == '7':
            self.weight = 7
        elif rank == '8':
            self.weight = 8
        elif rank == '9':
            self.weight = 9
        elif rank == 'T':
            self.weight = 10
        elif rank == 'J':
            self.weight = 11
        elif rank == 'Q':
            self.weight = 12
        elif rank == 'K':
            self.weight = 13
        elif rank == 'A':
            self.weight = 14
        else:
            print('Error')






#Kort kaladė
#Korta: objektas
#rank (2-9, T, J, Q, K, A)
#suit (spades, clubs, hearts, diamonds)
#sign (suit + rank)
#weight
#Kortų kaladė
<<<<<<< HEAD
#cards - sąrašas kortų
#shuffle
#take from top
#take from bottom
=======
 #cards - sąrašas kortų
 #shuffle
#take from top
 #take from bottom
>>>>>>> main
#take random
#mastom apie žaidimą