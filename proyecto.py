import random as r
def obtenerPreguntasPorCategoriaConRespuesta():
    preguntas = cargarDatos("preguntas.dat")
    for i in range(0, 7):
        pregunta = r.randint(0, len(preguntas[i])-1)
        print(preguntas[i][pregunta][0])
        print("Respuesta: ", preguntas[i][pregunta][1])

def obtenerPreguntaAleatoriaPorCategoria(categoria):
    preguntas  = cargarDatos("preguntas.dat")
    pregunta  = r.randint(0, len(preguntas[categoria])-1)
    print(preguntas[categoria][pregunta][0])
    print("Respuesta: ", preguntas[categoria][pregunta][1])
def tablaPuntuaciones():
    datosAciertos = cargarDatos("juegosDeUsuarios.dat")
    datosFallos = cargarDatos("fallosPorJugador.dat")
    for i, j in datosAciertos.items():
        print(f"{i} acertó {j} preguntas y falló {datosFallos[i]}")
        print("Promedio: ", (j/(j+datosFallos[i]))*100, "%")
def estadisticasPorJugador(jugador):
    datos = cargarDatos("juegosDeUsuarios.dat")
    datosVictorias = cargarDatos("ganadores.dat")
    print(f"Las estadísticas de {jugador} son: ")
    try:
        print(f"Cantidad de juegos: {datos[jugador]}")
    except:
        print("Este jugador aún no se encuentra registrado.")
    try:
        print(f"Cantidad de victorias: {datosVictorias[jugador]}")
    except:
        print(f"{jugador} aún no ha ganado ninguna partida.")
def topJugadores():
    datos = cargarDatos("juegosDeUsuarios.dat")
    print("Los jugadores con más juegos son: ")
    datosOrdenados = sorted(datos.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, len(datosOrdenados)):
        print(f"{i+1}. {datosOrdenados[i][0]} Cantidad de juegos: {datosOrdenados[i][1]}")
def topPreguntasFalladas():
    datos = cargarDatos("preguntasFalladas.dat")
    print("Las preguntas más falladas son: ")
    datosOrdenados = sorted(datos.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, len(datosOrdenados)):   
        print(f"{i+1}. {datosOrdenados[i][0]} Cantidad de fallos: {datosOrdenados[i][1]}")

def addRegistroJugadasPorJugador(datos, nombre):
    try:
        datos[nombre] += 1
    except:
        datos[nombre] = 1
    return datos
def addPreguntasFalladas(pregunta, datos):
    try:
        datos[pregunta] += 1
    except:
        datos[pregunta] = 1
    return datos
def guardarPreguntaFallada(archivo, datos):
    archivo = open(archivo, "w")
    archivo.write(str(datos))
    archivo.close()
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
    while contadorRondas < 30:
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
            datosPreguntasAcertadas = cargarDatos("preguntasAcertadas.dat")
            addRegistroJugadasPorJugador(datosPreguntasAcertadas, datosJugadores[turno][0])
            guardarPreguntaFallada("preguntasAcertadas.dat", datosPreguntasAcertadas)

        else:
            print("Respuesta incorrecta")
            falladas = cargarDatos("preguntasFalladas.dat")
            falladasCargadas = addPreguntasFalladas(preguntas[seccion][pregunta][0], falladas)
            guardarPreguntaFallada("preguntasFalladas.dat", falladasCargadas)
            datosFallosPorJugador = cargarDatos("fallosPorJugador.dat")
            addRegistroJugadasPorJugador(datosFallosPorJugador, datosJugadores[turno][0])
            guardarPreguntaFallada("fallosPorJugador.dat", datosFallosPorJugador)
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
        ganadores = cargarDatos("ganadores.dat")
        addRegistroJugadasPorJugador(ganadores, ganador)
        guardarPreguntaFallada("ganadores.dat", ganadores)
    for i in range(0, cantJugadores):
        #haz que se muestre la cantidad de preguntas acertadas por cada jugador. Haz que se muestre el porcentaje
        print(f"{datosJugadores[i][0]} acertó {datosJugadores[i][2]} preguntas ({(datosJugadores[i][2]/preguntasPorJugador)*100}%)")
    for i in range(0,len(datosJugadores)):
        datosCargados = cargarDatos("juegosDeUsuarios.dat")
        datoActualizado = sumarJuegoAJugador(datosJugadores[i][1], datosCargados)
        escribirDatos("juegosDeUsuarios.dat", datoActualizado)

    return 



def cargarDatos(archivo):
    archivo = open(archivo, "r")
    preguntas = archivo.read()
    archivo.close()
    return eval(preguntas)
def menu():
    print("""
        TRIVIAINFO
        1. Nuevo juego
        2. Consultas
        3. Reportes
        4. Salir
        """)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        iniciarJuego()
    elif opcion == 2:
        print("""
        1. Fallos por pregunta
        2. Juegos por jugador
        3. Estadísticas por jugador
        """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            topPreguntasFalladas()
        elif opcion == 2:
            topJugadores()
        elif opcion == 3:
            nombre = input("Ingrese el nombre del jugador: ").lower()
            estadisticasPorJugador(nombre)
        menu()
    elif opcion == 3:
        print("""
        1. Puntajes de jugadores
        2. Preguntas de una categoría
        3. Pregunta aleatoria
            """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            tablaPuntuaciones()
        elif opcion == 2:
            print("""Categorías: 
                  1. Conversión de decimal a binario
                  2. Conversión de decimal a octal
                  3. Conversión de decimal a hexadecimal
                  4. Conversión de binario a octal
                  5. Conversión de binario a hexadecimal
                  6. Conversión de binario a decimal
                  7. Operaciones aritméticas""")
            opcion = int(input("Ingrese una opción: "))-1
            obtenerPreguntaAleatoriaPorCategoria(opcion)
        elif opcion == 3:
            obtenerPreguntasPorCategoriaConRespuesta()
        menu()
    elif opcion == 4:
        print("Juego terminado. ")
        exit()
menu()

