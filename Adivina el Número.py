from random import *

#Función juego Adivina el número
def adivina_el_numero():
    print("Esto es Adivina El Número\nVoy a elegir un número del 1 al 100 y deberás adivinarlo\n¿Cuál es?")
    #La compu elige un número al azar
    numero_incognita = randint(1, 100)
    
    while True:
        #El jugador elige un número
        numero_jugador = int(input("Dime un número del 1 al 100"))

        #Prueba número
        if numero_jugador == numero_incognita:
            print("GANASTE")
            break
        else:
            if numero_jugador > numero_incognita:
                print ("El número elegido es mayor")
            else:
                print ("El número elegido es menor")

adivina_el_numero()