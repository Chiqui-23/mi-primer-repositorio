#JUEGO TA-TE-TI

#Defino la matriz
matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

#Imprimir la matriz
def imprimir_matriz_actual():
    print("\nMatriz Actual:")
    print("-------------")
    for fila in matriz:
        print(fila)
        
#El jugador 1 elije posición de la "X"
def juega_1():
    jugador_1_fila = int(input("Jugador 1: Elija fila 0, 1 o 2 donde va a colocar su ficha"))
    if jugador_1_fila == 0 or jugador_1_fila == 1 or jugador_1_fila == 2:
        jugador_1_columna = int(input("Jugador 1: Elija columna 0, 1 o 2 donde va a colocar su ficha"))
        if jugador_1_columna == 0 or jugador_1_columna == 1 or jugador_1_columna == 2:
            if matriz[jugador_1_fila][jugador_1_columna] == " ":
                matriz[jugador_1_fila][jugador_1_columna] = "X"
                imprimir_matriz_actual()
            else:
                print("Lugar ocupado, elija otro")
                juega_1()
        else:
            print("El número elegido debe ser 0, 1 o 2")
            juega_1()   
    else:
        print("El número elegido debe ser 0, 1 o 2")
        juega_1()
    
    
#El jugador 2 elije posición de la "O"
def juega_2():
    jugador_2_fila = int(input("Jugador 2: Elija fila 0, 1 o 2 donde va a colocar su ficha"))
    if jugador_2_fila == 0 or jugador_2_fila == 1 or jugador_2_fila == 2:
        jugador_2_columna = int(input("Jugador 2: Elija columna 0, 1 o 2 donde va a colocar su ficha"))
        if jugador_2_columna == 0 or jugador_2_columna == 1 or jugador_2_columna == 2:
            if matriz[jugador_2_fila][jugador_2_columna] == " ":
                matriz[jugador_2_fila][jugador_2_columna] = "O"
                imprimir_matriz_actual()
            else:
                print("Lugar ocupado, elija otro")
                juega_2()
        else:
            print("El número elegido debe ser 0, 1 o 2")
            juega_2()   
    else:
        print("El número elegido debe ser 0, 1 o 2")
        juega_2()
        
#Defino si ganó jugador 1
def ganador1():
    for fila in matriz:
        if fila == ["X", "X", "X"]:
            return True
    if matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
        return True
    elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
        return True
    elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
        return True
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
        return True
    elif matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
        return True   
    else:
        return False

#Defino si ganó jugador 2
def ganador2():
    for fila in matriz:
        if fila == ["O", "O", "O"]:
            return True
    if matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O":
        return True
    elif matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O":
        return True
    elif matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
        return True
    elif matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
        return True
    elif matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
        return True     
    else:
        return False

# Pruebo si hay empate
def empate():
    for fila in matriz:
        for columna in fila:
            if columna == " ":
                return False #hay un lugar disponible, se sigue jugando
    return True #No hay lugar disponible           

#Función juego Ta-Te-Ti
def TaTeTi():
    print("Bienvenido al juego Ta-Te-Ti")
    print("\nJugador 1  es 'X'\nJugador 2 es 'O'")
    imprimir_matriz_actual()
    
    while True:
        juega_1()
        if ganador1() == True:
            print("Gana el jugador 1")
            break
        if empate() == True:
            print("EMPATE - GAME OVER")
            break
        
        juega_2()    
        if ganador2() == True:
            print("Gana el jugador 2")
            break
        if empate() == True:
            print("EMPATE - GAME OVER")
            break
        
TaTeTi()