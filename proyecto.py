import random as r
def escribirDatos(archivo, datos):
    archivo = open(archivo, "w")
    archivo.write(str(datos))
    archivo.close()
def sumarJuegoAJugador(jugador, datos):
    try :
        datos[jugador] += 1
    except:
        datos[jugador] = 1
    return datos
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
            datosJugadores.append([jugador1, nickJ1, 0, nombreEquipo])
            datosJugadores.append([jugador2, nickJ2, 0])
    elif equipos == "n":
        tipoJuego = False
        print("El juego será individual. ")
        cantJugadores = int(input("Ingrese la cantidad de jugadores: "))
        for i in range(0, cantJugadores):
            nombre = input("Ingrese el nombre del jugador: ").lower()
            nick = input("Ingrese el nick del jugador: ").lower()
            datosJugadores.append([nombre, nick, 0])
    preguntas = cargarDatos("preguntas.dat")
    contadorRondas = 0
    preguntasJugadas = []
    turno = 0
    preguntasPorJugador = 0
    while contadorRondas < 5:
        if turno == cantJugadores:
            turno = 0
            preguntasPorJugador += 1
        while True:
            seccion = r.randint(0,6)
            pregunta = r.randint(0, len(preguntas[seccion])-1)
            if not preguntas[seccion][pregunta][0] in preguntasJugadas:
                break
        preguntasJugadas.append(preguntas[seccion][pregunta][0])
        print(f"Turno para {datosJugadores[turno][1]}")
        print(f"{contadorRondas}. {preguntas[seccion][pregunta][0]}")
        contadorRondas += 1
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == preguntas[seccion][pregunta][1]:
            print("Respuesta correcta")
            datosJugadores[turno][2] += 1
        else:
            print("Respuesta incorrecta")
        turno += 1
    if tipoJuego:
        sumaEquipo1 = datosJugadores[0][2] + datosJugadores[1][2]
        sumaEquipo2 = datosJugadores[2][2] + datosJugadores[3][2]
        if sumaEquipo1 > sumaEquipo2:
            print(f"¡El equipo {datosJugadores[0][3]} gana!")
        elif sumaEquipo1 < sumaEquipo2:
            print(f"¡El equipo {datosJugadores[2][3]} gana!")
        else:
            print("¡Ocurrió un empate!")
    else:
        maximo = 0
        for i in range(0, len(datosJugadores)):
            if datosJugadores[i][2] > maximo:
                maximo = datosJugadores[i][2]
                ganador = datosJugadores[i][0]
        print(f"¡{ganador} gana!")
    for i in range(0, cantJugadores):
        #haz que se muestre la cantidad de preguntas acertadas por cada jugador. Haz que se muestre el porcentaje
        print(f"{datosJugadores[i][0]} acertó {datosJugadores[i][2]} preguntas ({(datosJugadores[i][2]/preguntasPorJugador)*100}%)")
    for i in range(0,len(datosJugadores)):
        datosCargados = cargarDatos("juegosDeUsuarios.dat")
        datoActualizado = sumarJuegoAJugador(datosJugadores[i][1], datosCargados)
        escribirDatos("juegosDeUsuarios.dat", datoActualizado)

    return contadorRondas



def cargarDatos(archivo):
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
print(iniciarJuego())

