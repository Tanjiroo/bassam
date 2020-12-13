__author__ = "7396443, Almuhammad"


import random

def wuefeln():
    x = random.randint(1,6)
    return x




class Person:
    def __init__(self, name):
        self.name = name
    



#print(wuefeln())




anzahl_der_spieler = int(input("Please enter a number of players: "))
player = []
for i in range(anzahl_der_spieler):
    print("Please enter the name of", i, ". player")
    player_name = input("Player's name: ")
    i = Person(player_name)
    player.append(i)






    
