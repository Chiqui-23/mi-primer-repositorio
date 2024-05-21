import sys
import cowsay
import threading
import time

#Creo la clase Tamagotchi
class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 50
        self.nivel_felicidad = 50
        self.humor = ""
        self.esta_vivo = self.esta_vivo()
        
        #Creo la variable que controla el tiempo y largo el tiempo (run_tiempo)
        self.condicion_salida = threading.Event()
        self.hilo_tiempo = threading.Thread(target=self.run_tiempo)
        self.hilo_tiempo.start()

    #Función que reduce niveles de energía y aumenta niveles de hambre con el paso del tiempo    
    def run_tiempo(self):
        self.condicion_salida.clear()
        while not self.condicion_salida.is_set():
            time.sleep(5)
            self.nivel_energia -= 1
            self.nivel_hambre += 1
            self.muerte()
            if not self.esta_vivo:
                break

    #Función que modifica el humor
    def check_humor(self):
        if 0 < self.nivel_felicidad < 25 or 75 < self.nivel_hambre <= 100:
            self.humor = "Enojado"
        elif 25 <= self.nivel_felicidad < 50 or 50 < self.nivel_hambre < 75:
            self.humor = "Triste"
        elif self.nivel_felicidad == 50 or self.nivel_hambre == 50:
            self.humor = "Indiferente"
        elif 50 < self.nivel_felicidad <= 75 and self.nivel_hambre < 50:
            self.humor = "Feliz"
        elif 75 < self.nivel_felicidad <= 100 and self.nivel_hambre < 50:
            self.humor = "Eufórico"
        elif self.nivel_felicidad == 0:
            self.humor = "RIP"
        if self.nivel_energia < 15:
            self.humor = "Cansado"

    #Mostrar_estado: Muestra el nombre del Tamagotchi y sus niveles actuales de energía, hambre y humor. También dueño y tipo de tamagotchi.
    def mostrar_estado(self, nombre_usuario, tipo):
        self.check_humor()
        print("Estado actual: ")
        print("------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo de Tamagotchi: {tipo}")
        print(f"Dueño: {nombre_usuario}")
        print(f"Energía: {self.nivel_energia}")
        print(f"Hambre: {self.nivel_hambre}")
        print(f"Humor: {self.humor}")
        print("------------------")
        input("Presione ENTER para continuar")
        self.muerte()
        
    #Alimentar: Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
    def alimentar(self):
        #Hambre (baja)
        if self.nivel_hambre >= 10:    
            self.nivel_hambre -= 10
        elif self.nivel_hambre < 10:
            self.nivel_hambre = 0
        #Energía (baja)
        if self.nivel_energia >= 15:    
            self.nivel_energia -= 15
        elif self.nivel_energia < 15:
            self.nivel_energia = 0
            self.muerte()
        print(f"{self.nombre} está comiendo!")
        print("...")
        print("......")
        print(".........")
        print(f"{self.nombre} terminó de comer!")
        print("Hambre -10\nEnergía -15")
        print("------------------")
        input("Presione ENTER para continuar")

    #Jugar: Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel de hambre en 10.
    def jugar(self):
        self.mucha_hambre()
        #Felicidad (sube)
        if self.nivel_felicidad <= 80:    
            self.nivel_felicidad += 20
        elif self.nivel_felicidad > 80:
            self.nivel_felicidad = 100
        #Energía (baja)
        if self.nivel_energia >= 18:    
            self.nivel_energia -= 18
        elif self.nivel_energia < 18:
            self.nivel_energia = 0
            self.muerte()
        #Hambre (sube)
        if self.nivel_hambre <= 90:    
            self.nivel_hambre += 10
        elif self.nivel_hambre > 90:
            self.nivel_hambre = 100
        print(f"{self.nombre} está jugando!")
        print("...")
        print("......")
        print(".........")
        print(f"{self.nombre} terminó de jugar!")
        print("Felicidad +20\nEnergía -18\nHambre +10")
        print("------------------")
        input("Presione ENTER para continuar")

    #Dormir: Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5.
    def dormir(self):
        self.mucha_hambre_y_dormir()
        #Energía (sube)
        if self.nivel_energia <= 60:    
            self.nivel_energia += 40
        elif self.nivel_energia > 60:
            self.nivel_energia = 100
        #Hambre (sube)
        if self.nivel_hambre <= 95:    
            self.nivel_hambre += 5
        elif self.nivel_hambre > 95:
            self.nivel_hambre = 100
        print(f"{self.nombre} está durmiendo!")
        print("...")
        print("......")
        print(".........")
        print(f"{self.nombre} se despertó!")
        print("Hambre +5\nEnergía +40")
        print("------------------")
        input("Presione ENTER para continuar")

    #Verificar estado: revisa si el Tamagotchi está vivo.
    def verificar_estado(self):
        if self.nivel_energia != 0:
            print(f"{self.nombre} está vivo!")
            print("------------------")
            input("Presione ENTER para continuar")
        else:
            print(f"{self.nombre} murió :(")
            input("------------------")
            sys.exit()
            

    #Función Hambre >= 80.
    def mucha_hambre(self):
        if self.nivel_hambre >= 80:
            print(f"{self.nombre} tiene mucha hambre ...")
            #Felicidad (baja)
            if self.nivel_felicidad >= 30:    
                self.nivel_felicidad -= 30
            elif self.nivel_felicidad < 30:
                self.nivel_felicidad = 0
            #Energía (baja)
            if self.nivel_energia >= 20:    
                self.nivel_energia -= 20
            elif self.nivel_energia < 20:
                self.nivel_energia = 0
                self.muerte()
            print("Felicidad -30\nEnergía -20\n")

    #Función Hambre >= 80 y lo mandan a dormir
    def mucha_hambre_y_dormir(self):
        if self.nivel_hambre >= 80:
            print(f"{self.nombre} tiene mucha hambre ...")
            #Felicidad (baja)
            if self.nivel_felicidad >= 30:    
                self.nivel_felicidad -= 30
            elif self.nivel_felicidad < 30:
                self.nivel_felicidad = 0
            #Energía (baja)
            if self.nivel_energia > 80:    
                self.nivel_energia -= 80
                print("Felicidad -30\nEnergía -80\n")
            elif 80 >= self.nivel_energia >= 60:    
                self.nivel_energia -= 60
                print("Felicidad -30\nEnergía -60\n")
            elif 60 > self.nivel_energia > 40:    
                self.nivel_energia -= 40
                print("Felicidad -30\nEnergía -40\n")
            elif self.nivel_energia <= 40:
                self.nivel_energia = 0
                self.muerte()

    #Muerte
    def muerte(self):
        if self.nivel_energia == 0:
            self.nivel_hambre = 0
            self.nivel_felicidad = 0
            self.esta_vivo = False
            self.verificar_estado()
            
    
    #Función que verifica si el Tamagotchi está vivo
    def esta_vivo(self):
        if self.nivel_energia == 0:
            return False
        else:
            return True

#Menú del juego
def menu():
    print("")
    print("Elige una opción:\n ")
    print("1. Mostrar estado")
    print("2. Alimentar")
    print("3. Jugar")
    print("4. Dormir")
    print("5. Verificar estado")
    print("6. Salir")
    print("-------------------")

#Elección del Tamagotchi
def mostrar_tipos():
    print("")
    print("Elige un Tamagotchi:\n ")
    print("1. Vaca")
    print("2. Dragón")
    print("3. Zorro")
    print("4. Tigre")
    print("5. Chancho")
    print("6. Estegosauro")
    print("7. Tiranosauro")
    print("8. Pingüino")
    print("9. Tortuga")
    print("-------------------")

#Juego Tamagotchi --main
def main():
    print("BIENVENIDO A TAMAGOTCHI")
    print("-----------------------")
    
    #Nombre del Tamagotchi
    nombre = input("Introduce el nombre de tu Tamagotchi: ")
    print("")
    
    #Nombre del usuario
    nombre_usuario = input("Introduce tu nombre: ")
    
    #Genero el Tamagotchi
    mi_tamagotchi = Tamagotchi(nombre)
    
    #Elección del tipo de Tamagotchi
    tipo = ""
    while True:    
        mostrar_tipos()
        seleccion_tipo = input("")
        if seleccion_tipo == "1":
            cowsay.cow(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Vaca"
            break
        elif seleccion_tipo == "2":
            cowsay.dragon(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Dragón"
            break
        elif seleccion_tipo == "3":
            cowsay.fox(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Zorro"
            break
        elif seleccion_tipo == "4":
            cowsay.kitty(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Tigre"
            break
        elif seleccion_tipo == "5":
            cowsay.pig(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Chancho"
            break
        elif seleccion_tipo == "6":
            cowsay.stegosaurus(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Estegosauro"
            break
        elif seleccion_tipo == "7":
            cowsay.trex(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Tiranosauro"
            break
        elif seleccion_tipo == "8":
            cowsay.tux(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Pingüino"
            break
        elif seleccion_tipo == "9":
            cowsay.turtle(f"Hola {nombre_usuario}, bienvenido!!! Mi nombre es {nombre}. ¿Qué querés hacer?")
            tipo = "Tortuga"
            break
        else:
            print("Opción no válida, por favor elige otra.")
    
    #Función que hace al tamagotchi hablar según el tipo
    def tamagotchi_hablar(frase):
        if seleccion_tipo == "1":
            cowsay.cow(frase)
        elif seleccion_tipo == "2":
            cowsay.dragon(frase)
        elif seleccion_tipo == "3":
            cowsay.fox(frase)
        elif seleccion_tipo == "4":
            cowsay.kitty(frase)
        elif seleccion_tipo == "5":
            cowsay.pig(frase)
        elif seleccion_tipo == "6":
            cowsay.stegosaurus(frase)
        elif seleccion_tipo == "7":
            cowsay.trex(frase)
        elif seleccion_tipo == "8":
            cowsay.tux(frase)
        elif seleccion_tipo == "9":
            cowsay.turtle(frase)
    
    #Juego
    while mi_tamagotchi.esta_vivo:
        #Chequeo que esté vivo
        mi_tamagotchi.muerte()
        
        #Chequeo niveles de energía y hambre:        
        while True:
            if mi_tamagotchi.nivel_energia < 30:
                tamagotchi_hablar("Tengo sueño")
                break
            elif mi_tamagotchi.nivel_hambre > 70:
                tamagotchi_hablar("Tengo hambre")
                break
            elif mi_tamagotchi.nivel_felicidad < 25:
                tamagotchi_hablar("Estoy triste")
                break
            elif 25 <= mi_tamagotchi.nivel_felicidad < 65:
                tamagotchi_hablar("Estoy aburrido")
                break
            elif mi_tamagotchi.nivel_felicidad >= 80:
                tamagotchi_hablar("Estoy contento")
                break
            else:
                break
        
        #Menú
        menu()
        opcion = input("")
        
        if opcion == "1":
            mi_tamagotchi.mostrar_estado(nombre_usuario, tipo)
        elif opcion == "2":
            mi_tamagotchi.alimentar()
        elif opcion == "3":
            mi_tamagotchi.jugar()
        elif opcion == "4":
            mi_tamagotchi.dormir()
        elif opcion == "5":
            mi_tamagotchi.verificar_estado()
        elif opcion == "6":
            print("Gracias por jugar!")
            break
        else:
            print("Opción no válida, por favor elige otra.")

if __name__ == "__main__":
    main()