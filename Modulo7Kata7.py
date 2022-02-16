### Ejercicio 1: Creación de un ciclo "while"
new_planet = ''
planets = []


### Ejercicio 1: Uso de ciclos while en Python
while new_planet != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Ingresa un nuevo planeta para continuar o la palabra done para terminar\n")

### Ejercicio 2: Creación de un ciclo "for"
for planet in planets:
    print(planet)