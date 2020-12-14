__author__ = "7396443, Almuhammad"

import os
import random
import time
print("==========\n"
      "16-ist-tot\n"
      "==========")

time.sleep(0.5)

print ("Ziel des Spiels:\n"
"Es wird reihum gewürfelt.\n"
"Jeder darf so oft würfeln wie er will.\n"
"Wenn man nicht mehr würfeln will,\n"
"gibt man den Würfel weiter an den nächsten und dieser ist dran\n"
"Ziel ist es, durch mehrmaliges Würfeln und\n"
"aufsummieren der Würfelergebnisse \n"
"so nahe an 16 wie möglich zu kommen. \n")

print("Regeln des Spiels:\n")

time.sleep(1.0)

print("-Wer 16 oder mehr erreicht, hat sofort verloren\n"
      "-Wer als Summenpunkte 9 erreicht, darf nicht mehr würfeln\n"
      "-Wer als Summenpunkte 10 erreicht, muss noch einmal werfen\n")

time.sleep(1.0)


def wuefeln():
    """rtuzutzizu"""
    x = random.randint(1,6)
    return x



def neustart():
    neustart = input("Willst du noch eine Runde spielen? Ja[Y], Nein[N]\n")
    
    if neustart == "y":
        main()
    else:
        neustart()




class Person:
    """rkjrhtre"""
    def __init__(self, name):
        self.name = name
        self.punkte = 0

    def sum(self, punkt):
        self.punkte += punkt
    
"""
def clear(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 


"""

anzahl_der_spieler = int(input("Please enter a number of players: "))
player = []
for i in range(1, anzahl_der_spieler+1):
    print("Please enter the name of", i, ". player")
    player_name = input("Player's name: ")
    i = Person(player_name)
    player.append(i)










def main():
    """zrtzurzizu"""
    rounde = 1
    while len(player) != 1:
        if rounde == len(player):
            rounde = 0
        print("Spieler ", player[rounde-1].name, "am Zug")
        
        wuerfel = wuefeln()
        player[rounde-1].sum(wuerfel)
        print(wuerfel)
        while True:
            frage = input("Wollen Sie Nochmal Würfeln: ")
            if frage == "y":
                wuerfel = wuefeln()
                player[rounde-1].sum(wuerfel)
                print(wuerfel)
                print("Summe der Punkte", player[rounde-1].punkte)
                if player[rounde-1].punkte == 9:
                    print("Du hast 9 bekommen dann du darfst nicht mehr würfeln")
                    break
                if player[rounde-1].punkte == 10:
                    print("Du hast eine 10 dann du musst nochmal würfeln")
                    time.sleep(3.0)
                    wuerfel = wuefeln()
                    player[rounde-1].sum(wuerfel)
                    print(wuerfel)
                    print("Summe der Punkte", player[rounde-1].punkte)
                

                
                elif player[rounde-1].punkte > 15:
                    print("Du hast verloren")
                    player.remove(player[rounde-1])
                    rounde -= 1
                    break

            elif frage == "n":
                break
                     
                
                

            
          

        if len(player) == 1:
            print("Gratuliere ", player[rounde-1].name, "Du hast gewonnen.")
                

        #player[rounde-1].punkte = 0
            
        rounde += 1

        
if __name__ == "__main__":
   main()


    

        



        
        



    
