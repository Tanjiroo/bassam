__author__ = "7396443, Almuhammad"


import random

def wuefeln():
    x = random.randint(1,6)
    return x




class Person:
    def __init__(self, name):
        self.name = name
        self.punkte = 0

    def sum(self, punkt):
        self.punkte += punkt
    



#print(wuefeln())




anzahl_der_spieler = int(input("Please enter a number of players: "))
player = []
for i in range(1, anzahl_der_spieler+1):
    print("Please enter the name of", i, ". player")
    player_name = input("Player's name: ")
    i = Person(player_name)
    player.append(i)




def game():

    rounde = 1
    while len(player) != 1:
        if rounde == len(player):
            rounde = 0
        print("Spieler ", player[rounde-1].name, "am Zug")
        anzahl_der_wuerfeln = int(input("Wie oft möchtest du würfeln: "))
        for i in range(anzahl_der_wuerfeln):
            wuerfel = wuefeln()
            player[rounde-1].sum(wuerfel)
            print(wuerfel)
        if player[rounde-1].punkte == 10:
            print("Du hast eine 10 dann du musst nochmal würfeln")
            wuerfel = wuefeln()
            player[rounde-1].sum(wuerfel)
            print(wuerfel)
            
        print("Summe der Punkte", player[rounde-1].punkte)
        elif player[rounde-1].punkte == 9:
            print("Du hast verloren")
            player.remove(player[rounde-1])
            rounde -= 1
            
        elif player[rounde-1].punkte >= 16:
            print("Du hast verloren")
            player.remove(player[rounde-1])
            rounde -= 1

        if len(player) == 1:
            print("Gratuliere ", player[rounde-1].name, "Du hast gewonnen.")

        #player[rounde-1].punkte = 0
        







        
        
        rounde += 1


game()
    
