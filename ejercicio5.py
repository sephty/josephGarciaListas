'''
Nombre: Joseph Garcia Jimenez
fecha: 2025-07-20
Descripción: Programa para contar vocales.
'''

frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")
