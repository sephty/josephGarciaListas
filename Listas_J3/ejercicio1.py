'''
Nombre: Joseph Garcia Jimenez
fecha: 2025-07-20
descripción: Programa de gestion de caracteres.
'''

frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")