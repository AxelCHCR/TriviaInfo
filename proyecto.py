import random as r
def iniciarJuego():
    equipos = input("¿Hay equipos? (s/n): ").lower()
    tipoJuego = None #True para juego en equipo, False para juego individual
    datosJugadores = []
    if equipos == "s":
        print("Para que el juego sea justo, ambos equipos serán de dos jugadores. ")
        tipoJuego  = True
        cantJugadores = 4
        for i in range(1,3):
            print(f"Datos para el equipo {i}. ")
            nombreEquipo = input("Ingrese el nombre del equipo: ").lower()
            jugador1 = input("Ingrese el nombre del primer jugador: ").lower()
            nickJ1 = input("Ingrese el nick del primer jugador: ").lower()
            jugador2 = input("Ingrese el nombre del segundo jugador: ").lower()
            nickJ2 = input("Ingrese el nick del segundo jugador: ").lower()
            datosJugadores.append([jugador1, nickJ1, 0])
            datosJugadores.append([jugador2, nickJ2, 0])
    elif equipos == "n":
        tipoJuego = False
        print("El juego será individual. ")
        cantJugadores = int(input("Ingrese la cantidad de jugadores: "))
        for i in range(0, cantJugadores):
            nombre = input("Ingrese el nombre del jugador: ").lower()
            nick = input("Ingrese el nick del jugador: ").lower()
            datosJugadores.append([nombre, nick, 0])
    preguntas = cargarPreguntas("preguntas.dat")
    contadorRondas = 0
    preguntasJugadas = []
    while contadorRondas < 30:
        while True:
            seccion = r.randint(0,6)
            pregunta = r.randint(0, len(preguntas[seccion])-1)
            if not preguntas[seccion][pregunta][0] in preguntasJugadas:
                break
        preguntasJugadas.append(preguntas[seccion][pregunta][0])
        print(f"{contadorRondas}. {preguntas[seccion][pregunta][0]}")
        contadorRondas += 1
        
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == preguntas[seccion][pregunta][1]:
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")
    return contadorRondas



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
        iniciarJuego()
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass

#menu()
print(iniciarJuego(1))

