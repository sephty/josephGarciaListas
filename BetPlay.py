'''
Nombre: Joseph Garcia Jimenez
fecha: 2025-07-20
Descripción: Programa de gestión de equipos tipo BetPlay.
'''


# from tabulate import tabulate

equipos = []
jugadores = []
partidos = []
  # (nombre, PJ, PG, PP, PE, GF, GC, TP)
def agregar_equipo():
    nombre = input("Nombre del equipo: ")
    equipo = (nombre, [0, 0, 0, 0, 0, 0, 0])
    equipos.append(equipo)
    print(f"Equipo '{nombre}' agregado.\n")

def agregar_jugador():
    nombre = input("Nombre del jugador: ")
    dorsal = input("Número en la espalda: ")
    edad = input("Edad: ")
    equipo = input("Equipo al que pertenece: ")
    jugador = (nombre, dorsal, edad, equipo, 0) 
    jugadores.append(jugador)
    print(f"Jugador '{nombre}' agregado.\n")

def registrar_partido():
    print("Registrar nuevo partido:")
    eq1 = input("Equipo 1: ")
    eq2 = input("Equipo 2: ")
    fecha = input("Fecha del partido: ")
    try:
        goles1 = int(input(f"Goles de {eq1}: "))
        goles2 = int(input(f"Goles de {eq2}: "))
    except ValueError:
        print("Ingrese un número válido para los goles.\n")
        return

    goleadores = []
    total_goles = goles1 + goles2
    for i in range(total_goles):
        nombre = input(f"Gol {i+1}. ¿Quién lo hizo?: ")
        goleadores.append(nombre)
        # Actualizar goles del jugador
        for j in range(len(jugadores)):
            if jugadores[j][0] == nombre:
                jugador = list(jugadores[j])
                jugador[4] += 1
                jugadores[j] = tuple(jugador)

    partidos.append((eq1, eq2, fecha, goles1, goles2, goleadores))
    actualizar_estadisticas(eq1, eq2, goles1, goles2)
    print("Partido registrado exitosamente.\n")

def actualizar_estadisticas(eq1, eq2, goles1, goles2):
    for i in range(len(equipos)):
        if equipos[i][0] == eq1 or equipos[i][0] == eq2:
            nombre, stats = equipos[i]
            stats[0] += 1  # PJ
            if nombre == eq1:
                stats[4] += goles1  # GF
                stats[5] += goles2  # GC
                if goles1 > goles2:
                    stats[1] += 1  # PG
                    stats[6] += 3
                elif goles1 < goles2:
                    stats[2] += 1  # PP
                else:
                    stats[3] += 1  # PE
                    stats[6] += 1
            else:
                stats[4] += goles2
                stats[5] += goles1
                if goles2 > goles1:
                    stats[1] += 1
                    stats[6] += 3
                elif goles2 < goles1:
                    stats[2] += 1
                else:
                    stats[3] += 1
                    stats[6] += 1
            equipos[i] = (nombre, stats)

def mostrar_estadisticas():
    '''usar_tabulate = input("¿Usar tabulate para mostrar? (s/n): ").lower()
    if usar_tabulate == "s":
        tabla = []
        for nombre, datos in equipos:
            fila = [nombre] + datos
            tabla.append(fila)
        print(tabulate(tabla, headers=["Equipo", "PJ", "PG", "PP", "PE", "GF", "GC", "TP"]))
    else:
    '''  
    for nombre, datos in equipos:
        print(f"{nombre} => PJ:{datos[0]} PG:{datos[1]} PP:{datos[2]} PE:{datos[3]} GF:{datos[4]} GC:{datos[5]} TP:{datos[6]}")
    print()

def mostrar_partidos():
    for partido in partidos:
        eq1, eq2, fecha, g1, g2, goleadores = partido
        print(f"{fecha}: {eq1} {g1} - {g2} {eq2}")
        print("Goleadores:", ", ".join(goleadores))
    print()

def mostrar_jugadores():
    for j in jugadores:
        print(f"{j[0]} | Dorsal: {j[1]} | Edad: {j[2]} | Equipo: {j[3]} | Goles: {j[4]}")
    print()

def main():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Agregar equipo")
        print("2. Agregar jugador")
        print("3. Registrar partido")
        print("4. Mostrar estadísticas de equipos")
        print("5. Mostrar partidos jugados")
        print("6. Mostrar jugadores")
        print("7. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.\n")
            continue

        match opcion:
            case 1:
                agregar_equipo()
            case 2:
                agregar_jugador()
            case 3:
                registrar_partido()
            case 4:
                mostrar_estadisticas()
            case 5:
                mostrar_partidos()
            case 6:
                mostrar_jugadores()
            case 7:
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida.\n")

if __name__ == "__main__":
    main()
 