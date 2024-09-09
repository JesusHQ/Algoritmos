import math


# Función que calcula el rango de edad compatible según las reglas dadas
def calcular_rango_edad(age):
    if age > 14:
        # Si la edad es mayor a 14, usamos la fórmula clásica
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Si la edad es 14 o menos, usamos la fórmula alternativa
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Pedir al usuario la edad por consola
age = int(input("Introduce tu edad: "))

# Calcular el rango de edad compatible
rango_edad = calcular_rango_edad(age)

# Mostrar el resultado
print(f"El rango de edad compatible es: {rango_edad}")
