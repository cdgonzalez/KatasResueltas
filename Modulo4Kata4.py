##### Ejercicio 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

phrase = text.split(".")
clue_word = ['average','temperature','distance']

## Hechos con palabras Clave
for item in phrase:
    for word in clue_word:
        if word in item:
            print(item)
            break

## Cambiando "C" a "Celsius"

for item in phrase:
    for word in clue_word:
        if word in item:
            if '127' in item:
                print(item.replace(' C', ' Celsius'))
                break



#### Ejercicio 2
#### Formateando Cadenas
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # en kms
planet = "Earth"

titulo = f"Hechos sobre la gravedad de {name}"
hechos = f"""-------------------------------
Nombre del Planeta: {planet}
Gravedad en {name}: {gravity*1000} m/s2"""

plantilla = f"""{titulo.title()}
{hechos}
"""
print(plantilla)


# Nuevos datos para la muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

nueva_plantilla = """Hechos sobre la gravedad de: {nombre}
---------------------------------------
Nombre del Planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2"""
print(nueva_plantilla.format(nombre=nombre,planeta=planeta,gravedad=gravedad*1000))