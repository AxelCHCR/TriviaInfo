import random as r
def iniciarJuego(cantJugadores):
    preguntas = cargarPreguntas("preguntas.dat")

def cargarPreguntas(archivo):
    archivo = open(archivo, "r")
    preguntas = archivo.read()
    archivo.close()
    return eval(preguntas)
def menu():
    print("""
        TRIVIAINFO
        1. Nuevo juego
        2. Marcadores
        3. Estadísticas
        4. Salir
        """)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        jugadores = int(input("Ingrese la cantidad de jugadores: "))
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass

#menu()
print(cargarPreguntas())

