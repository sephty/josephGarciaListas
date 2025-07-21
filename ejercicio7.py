'''
Nombre: Joseph Garcia Jimenez
fecha: 2025-07-20
Descripción: Programa de gestión de equipos tipo BetPlay.
'''

palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
print(f"La palabra invertida es: {invertida}")