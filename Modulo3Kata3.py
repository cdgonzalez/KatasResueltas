### Ejercicio - Escribir declaraciones if, else, y elif
from ast import If
from traceback import print_tb
from turtle import st


a = 5
b = 4
expresion_prueba = (a < b)

if expresion_prueba:
    print("La expresion: " + str(a) +" es menor que: " + str(b))
    c = 83
    d = (c%3)
    expresion_prueba2 = (d != 0)

    if expresion_prueba2:
        print("La operación de: " + str(c) + " modulo: 3 es igual a: "+ str(d))
        
        if d > 0:
            print("No es una división entera")
        else: 
            print("Es una división entera")
elif (a > b):
    print("La expresion: " + str(a) +" es mayor que: " + str(b))
else:
    print("La expresion: " + str(a) +" es igual que: " + str(b))

### Asteroide de 49 km/s
asteroid_vel = 49
print("Se dirige un Asteroide a la Tierra")
print("...")
print("...")
print("...")
print("Calculando Velocidad")
print("...")
print("...")
print("...")

if asteroid_vel > 25:
    print("¡Advertencia asteroide a mas de 25 km/s acercandose!")
else:
    print("No hay riesgo de colisión catastrofica por el asteroide detectado")


### Asteroide de 19 km/s
asteroide_menor = 19
if asteroid_vel >= 20:
    print("¡Peligro!")
    print("¡Peligro!")
    print("¡Peligro!")
    print("¡Un as de luz en el cielo!, se dirige un asteroide a mas de 20 km/s a la Tierra")
elif asteroid_vel == 19:
    print("¡Cuidado se dirige un asteroide de 19 km/s a la Tierra!")
else:
    print("Se dirige un asteroide con menos de 19 km/s de velocidad hacia la Tierra")


#### Ejercicio: Uso de operadores and y or
asteroid_size = 34567
asteroid_vel = 30

if asteroid_size > 25 and asteroid_vel >= 25:
    print("¡Peligro!")
    print("¡Peligro!")
    print("¡Peligro!")
    print("¡Final eminente asteroide de tamaño: " + str(asteroid_size) + " y con una velocidad: " + str(asteroid_vel) 
    + "detectado!")
elif asteroid_size > 25 or asteroid_vel > 25:
    print("¡Peligro!")
    print("¡Peligro!")
    print("¡Peligro!")
    print("¡Un asteroide de tamaño: " + str(asteroid_size) + " y con una velocidad: " + str(asteroid_vel)
    + "se dirige a la Tierra!")
elif asteroid_size > 25 and asteroid_vel < 25:
    print("¡Advertencia!")
    print("¡Advertencia!")
    print("¡Advertencia!")
    print("¡El asteroide presenta un tamaño irregular: " + str(asteroid_size) + " y una velocidad: " + str(asteroid_vel))
elif asteroid_size < 25 and asteroid_vel > 20:
    print("¡Precaución!")
    print("¡Precaución!")
    print("¡Precaución!")
    print("¡Alerta por un as de luz en el cielo asteroide de: " + str(asteroid_vel) +" km/s acercandose !")
else:
    print("Se detecto el ingreso de un asteroide a la atmosfera del planeta, pero no presenta riesgo alguno")