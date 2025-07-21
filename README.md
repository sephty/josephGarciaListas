[toc]



# Desarrollo de actividad

joseph Garcia Jimenez

Grupo: J3 campusland

fecha: 21 julio 2025

## Ejercicio 1





![](https://i.ibb.co/j9Bq50jY/Captura-desde-2025-07-21-13-58-55.png)

```
frase = input("Escribe una frase: ")
```

Esta línea le pide al usuario que escriba una frase. Lo que el usuario escriba se guarda en la variable frase.

```
total_caracteres = len(frase)
```

Usa la función len() para contar cuántos caracteres tiene la frase en total, incluyendo letras, espacios, signos, etc.

```
espacios = frase.count(" ")
```

Cuenta cuántos espacios hay en la frase con .count(" "). Solo cuenta los espacios en blanco, no otros caracteres.

```
print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")
```

Muestra por pantalla cuántos caracteres y espacios tiene la frase, usando f-strings para incluir los valores dentro del texto.



## Ejercicio 2



![](https://i.ibb.co/4RMNSyLM/Captura-desde-2025-07-21-13-59-01.png)

```
nombre = input("Escribe tu nombre completo: ")
```

Pide al usuario que escriba su nombre completo. Lo que escriba se guarda en la variable nombre.

```
if nombre.replace(" ", "").isalpha():
```


Esta línea revisa si el nombre solo tiene letras. Usa .replace(" ", "") para quitar los espacios y luego .isalpha() para comprobar que todo lo que queda son letras.
Por ejemplo, "Juan Pérez" se convierte en "JuanPérez" y se valida que no tenga números ni símbolos.

```
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
```

Si el nombre pasa la validación anterior, ahora verifica si cada palabra comienza con mayúscula, usando .istitle().
Ejemplo válido: "Juan Pérez"
Ejemplo no válido: "juan pérez"

despues, si alguna palabra no comienza con mayúscula, muestra este mensaje.

```
else:
    print("El nombre solo debe contener letras.")
```

Si el nombre contiene algo que no sea letra (como números o símbolos), muestra este mensaje.



## Ejercicio 3

![](https://i.ibb.co/G4CC9t2Z/Captura-desde-2025-07-21-13-59-07.png)

```
palabra = input("Escribe una palabra: ")
```

Pide al usuario que escriba una palabra y la guarda en la variable palabra.

```
invertida = palabra[::-1]
```

Usa el slicing con [::-1] para invertir la palabra. Esto crea una nueva cadena que es la original pero al revés.

```
print(f"La palabra invertida es: {invertida}")
```


Muestra en pantalla la palabra invertida usando una f-string para incluir la variable invertida dentro del texto.

## Ejercicio 4

![](https://i.ibb.co/ccRcDfsG/Captura-desde-2025-07-21-13-59-24.png)

```
frase = input("Escribe una frase: ")
```

Pide al usuario que escriba una frase y la guarda en la variable frase.

```
frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")
```

Reemplaza todas las vocales minúsculas (a, e, i, o, u) por el símbolo *.
Luego hace lo mismo con las vocales mayúsculas (A, E, I, O, U).

```
print(f"La frase cifrada es: {frase_cifrada}")
```

Muestra en pantalla la frase modificada, donde las vocales fueron sustituidas por *.



## Ejercicio 5



![](https://i.ibb.co/Dfk1KFWg/Captura-desde-2025-07-21-13-59-28.png)

```
frase = input("Escribe una frase: ")
```

Pide al usuario que escriba una frase y la guarda en la variable frase.

```
a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")
```

Cuenta cuántas veces aparece cada vocal, tanto en minúscula como en mayúscula, sumando ambos resultados.

```
total_vocales = a + e + i + o + u
```

Suma todas las cantidades de vocales para obtener el total.

```
print(f"La frase tiene {total_vocales} vocales.")
```


Muestra en pantalla el número total de vocales que tiene la frase.

## Ejercicio 6

![](https://i.ibb.co/DDL1Dx7V/Captura-desde-2025-07-21-13-59-37.png)

```
telefono = input("Escribe número de teléfono de 10 dígitos: ")
```

Pide al usuario que escriba un número de teléfono y lo guarda en la variable telefono.

```
if len(telefono) == 10 and telefono.isdigit():
```

Verifica que el número tenga exactamente 10 caracteres y que todos sean dígitos (no letras ni símbolos).

```
telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
```


Si la verificación es correcta, formatea el número así:

Los primeros 3 dígitos entre paréntesis, después un espacio, luego 3 dígitos, un guion, y los últimos 4 dígitos.
Ejemplo: (123) 456-7890

```
print(f"El número formateado es: {telefono_formateado}")
```

Muestra el número ya formateado.

```
    print("El número debe tener exactamente 10 dígitos.")
```

Si no cumple con la longitud o no es solo números, muestra un mensaje de error.

## Ejercicio 7

![https://i.ibb.co/cSv7B752/Captura-desde-2025-07-21-13-59-42.png](https://i.ibb.co/cSv7B752/Captura-desde-2025-07-21-13-59-42.png)

```
labra = input("Escribe una palabra: ").lower()
```

Pide al usuario que escriba una palabra, la convierte a minúsculas y la guarda en la variable palabra.

```
invertida = palabra[::-1]
```


Invierte la palabra usando slicing con [::-1] y guarda el resultado en invertida.

```
if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
```

Compara la palabra original con la invertida. Si son iguales, muestra que es un palíndromo; si no, dice que no lo es.

```
print(f"La palabra invertida es: {invertida}")
```


Finalmente, muestra la palabra invertida.