### Ejercicio1: Crear y usar listas de Python
planets = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

planets.append("Pluton")
print("El último planeta del Sistema Solar es: " + planets[-1])

### Ejercicio 2: Trabajando con datos de una lista
planetUser = input("Ingresa el nombre de un planeta con la primer letra en Mayúscula")
planetIndex = planets.index(planetUser)

### Planetas más cerca a partir del ingresado por el usuario
planetsBefore = planets[0:planetIndex]
print("Planetas más cerca al sol antes de: " + planetUser)
print(planetsBefore)

### Planetas más alejados a partir del ingresado por el usuario
planetsAfter = planets[planetIndex+1:]
print("Planetas más lejos al sol después de: " + planetUser)
print(planetsAfter)