### Ejercicio 1: Creación de diccionarios de Python

### Ejercicio: Crear y modificar un diccionario de Python

planet = {
    'name' : 'Marte',
    'moons' : 2
}

print(f"El Planeta: { planet['name'] } tiene { planet['moons'] } lunas.")

###polar: 6752
###equatorial: 6792
planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f"El Planeta: { planet['name'] } tiene { planet['circunferencia (km)']['polar'] } de circunferencia polar.")


### Ejercicio 2: Programación dinámica con diccionarios
### Ejercicio: Cálculo de valores
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
planets = len(planet_moons.keys())
total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

print(f"Cantidad de lunas en el sistema solar: {total_moons}")
promedio = total_moons / planets
print(f"Promedio de luna por planeta: {promedio}")