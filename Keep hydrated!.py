import math

# Función que calcula la cantidad de litros de agua que Nathan beberá durante el ciclismo
def calcular_litros(time):
    # Nathan bebe 0.5 litros por hora, redondeado hacia abajo al entero más cercano
    litres = math.floor(time * 0.5)
    return litres

# Pedir al usuario que ingrese el tiempo de ciclismo en horas
time = float(input("Introduce el tiempo de ciclismo en horas: "))

# Calcular los litros de agua que beberá
litros = calcular_litros(time)

# Mostrar el resultado
print(f"Nathan beberá {litros} litros de agua.")
