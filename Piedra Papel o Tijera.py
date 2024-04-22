#JUEGO PIEDRA, PAPEL O TIJERA

from random import *

def juego():
    
    #Elección del jugador
    print("Vamos a jugar a piedra, papel o tijera. Ingresa 0 para piedra, 1 para papel o 2 para tijera")
    jugador = int(input("Ingresa 0 para piedra, 1 para papel o 2 para tijera"))

    if jugador == 0:
        print ("Tu elección es piedra")
    elif jugador == 1:
        print ("Tu elección es papel")
    elif jugador == 2:
        print ("Tu elección es tijera")
    else:
        print ("Elije 0, 1 o 2")

    if jugador == 0 or jugador == 1 or jugador == 2:
            #Elección de la compu 
            compu = randint(0, 2)
            if compu == 0:
                print ("Mi elección es piedra")
            elif compu == 1:
                print ("Mi elección es papel")
            else:
                print ("Mi elección es tijera")
            
            #Resultado
            if jugador == compu:
                print("Empate")
            elif jugador == 0:
                if compu == 1:
                    print("Perdiste")
                else:
                    print("Ganaste")
            elif jugador == 1:
                if compu == 2:
                    print("Perdiste")
                else:
                    print("Ganaste")
            elif jugador == 2:
                if compu == 0:
                    print("Perdiste")
                else:
                    print("Ganaste")

juego()