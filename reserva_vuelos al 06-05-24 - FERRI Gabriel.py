#Código corregido por CHATGPT

import random
import cv2
import playsound

# Declaraciones
menu = '''
1 - Buscar vuelos
2 - Mostrar vuelos disponibles
3 - Comprar pasaje
4 - Salir
'''

paises = [
    "Estados Unidos", "Canadá", "México", "Brasil", "Argentina", 
    "Reino Unido", "Francia", "Alemania", "Italia", "España", 
    "China", "Japón", "India", "Australia", "Rusia", 
    "Sudáfrica", "Nigeria", "Egipto", "Turquía", "Corea del Sur"
]

fechas = [
    '30/04/2024', '31/06/2024', '15/08/2024', '20/10/2024', '25/12/2024',
    '05/02/2025', '10/04/2025', '20/06/2025', '15/08/2025', '30/10/2025',
    '25/12/2025', '20/02/2026', '15/04/2026', '10/06/2026', '05/08/2026',
    '20/10/2026', '15/12/2026', '10/02/2027', '05/04/2027', '30/06/2027'
]

opcionesAsientos = [100, 150, 200]
opcionesPrecios = [100000, 150000, 200000, 250000, 300000]

vuelos = []  # Lista de vuelos generados [Origen, Destino, Fecha, Asientos disponibles, N° de vuelo]

# Genero vuelos al azar
for i in range(10):
    a = random.choice(paises)
    b = random.choice(paises)
    if a != b:
        vuelos.append([a, b, random.choice(fechas), random.choice(opcionesAsientos), i+1])

def mostrar_menu():
    print('BIENVENIDO')
    print(menu)
    opcion = int(input('Seleccione una opción: '))
    
    if opcion == 1:
        buscar_vuelos()
    elif opcion == 2:
        mostrar_vuelos_disponibles()
    elif opcion == 3:
        comprar_pasaje()
    elif opcion == 4:
        print('Gracias por usar nuestro servicio')

def buscar_vuelos():
    print("Ingrese los datos para filtrar los vuelos disponibles:")
    origen = input('Ingrese el origen del vuelo: ')
    destino = input('Ingrese el destino del vuelo: ')
    
    for vuelo in vuelos:
        if vuelo[0].lower() == origen.lower() and vuelo[1].lower() == destino.lower():
            print('DATOS DEL VUELO:')
            print(f'Vuelo N°: {vuelo[4]}')
            print(f'Origen: {vuelo[0]}')   
            print(f'Destino: {vuelo[1]}') 
            print(f'Fecha: {vuelo[2]}')
            print(f'Asientos disponibles: {vuelo[3]}')
            print('--------------------')
    
    mostrar_menu()

def mostrar_vuelos_disponibles():
    print('Vuelos disponibles:')
    for vuelo in vuelos:
        print(f'Vuelo N°: {vuelo[4]}, Origen: {vuelo[0]}, Destino: {vuelo[1]}, Fecha: {vuelo[2]}, Asientos disponibles: {vuelo[3]}')
    mostrar_menu()


def mostrar_asientos(num_vuelo):
    for vuelo in vuelos:
        if vuelo[4] == num_vuelo:
            print(f'Asientos disponibles para el Vuelo N° {num_vuelo}, de {vuelo[0]} a {vuelo[1]} el día {vuelo[2]}:')
            asientos_disponibles = vuelo[3]
            filas = 10  # N° filas
            columnas = asientos_disponibles // filas
            matriz_asientos = [['O' for _ in range(columnas)] for _ in range(filas)]

            # Imprimir MATRIZ
            print('  ', ' '.join([str(i+1) for i in range(columnas)]))
            for fila in range(filas):
                print(f'{fila+1} ', ' '.join(matriz_asientos[fila]))

            while True:
                print('O: Asiento disponible')
                print('X: Asiento reservado')

                # Seleccionar asiento
                num_asiento = int(input(f'Ingrese el número de asiento (del 1 al {asientos_disponibles}) que desea reservar (0 para cancelar):'))
                
                if num_asiento == 0:
                    print('Operación cancelada')
                    mostrar_menu()
                    break

                if num_asiento > 0 and num_asiento <= vuelo[3]:
                    fila_asiento = (num_asiento - 1) // columnas
                    columna_asiento = (num_asiento - 1) % columnas

                    if matriz_asientos[fila_asiento][columna_asiento] == 'O':
                        # Marcar el asiento como reservado ('X') en la matriz
                        matriz_asientos[fila_asiento][columna_asiento] = 'X'
                        vuelo[3] -= 1  # Reducir el número de asientos disponibles
                        print(f'Asiento N° {num_asiento} reservado con éxito')
                        
                        # Mostrar matriz actualizada
                        print('  ', ' '.join([str(i+1) for i in range(columnas)]))
                        for fila in range(filas):
                            print(f'{fila+1} ', ' '.join(matriz_asientos[fila]))
                        
                        # Costo del pasaje
                        print(f'El costo del pasaje es de {random.choice(opcionesPrecios)}')
                        
                        # Confirmar compra
                        confirmar_compra(vuelo)
                        break
                    else:
                        print(f'El asiento N° {num_asiento} ya está reservado')
                else:
                    print('Número de asiento inválido')
            
            break


def comprar_pasaje():
    print('Ingrese los datos para comprar el pasaje:')
    numero_vuelo = int(input('Ingrese el número de vuelo: '))
    
    for vuelo in vuelos:
        if numero_vuelo == vuelo[4]:
            print(f'El vuelo seleccionado es: {vuelo[0]} a {vuelo[1]}, el día {vuelo[2]}')
            print('¿Es correcto?')
            print("1. Si")
            print("2. No")
            opcion_comprar = int(input("Seleccione una opción: "))
            
            if opcion_comprar == 1:
                mostrar_asientos(numero_vuelo)
                
                # Seleccionar asiento y confirmar compra
                print('Ingrese el número de asiento que desea reservar:')
                num_asiento = int(input())
                
                # Reducir el número de asientos disponibles si se confirma la compra
                if num_asiento > 0 and num_asiento <= vuelo[3]:
                    vuelo[3] -= 1
                    print(f'Su asiento es el N°{num_asiento}')
                    
                    # Mostrar costo del pasaje
                    print(f'El costo del pasaje es de {random.choice(opcionesPrecios)}')
                    
                    # Confirmar compra
                    confirmar_compra(vuelo)
                else:
                    print('Número de asiento inválido')
                    mostrar_menu()
            else:
                print('Compra cancelada')
                mostrar_menu()
            break  # Salir del bucle una vez que se encuentre el vuelo

def confirmar_compra(vuelo):
    print('¿Desea confirmar la compra?')
    print("1. Si")
    print("2. No")
    opcion_confirmar = int(input("Seleccione una opción: "))
    
    if opcion_confirmar == 1:
        #playsound.playsound("cash.mp3")
        cv2.imshow("Gracias", cv2.cvtColor(cv2.imread("GRACIAS.jpg"), cv2.COLOR_BGR2RGB))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('Compra realizada con éxito')
        mostrar_menu()
    else:
        print('Compra cancelada')
        mostrar_menu()
        

# MAIN
mostrar_menu()