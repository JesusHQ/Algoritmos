# Función que calcula el tercer ángulo de un triángulo
def tercer_angulo(angulo1, angulo2):
    # La suma de los ángulos de un triángulo siempre es 180 grados
    return 180 - (angulo1 + angulo2)

# Pedir los ángulos al usuario a través de la consola
angulo1 = int(input("Introduce el primer ángulo: "))
angulo2 = int(input("Introduce el segundo ángulo: "))

# Calcular el tercer ángulo
resultado = tercer_angulo(angulo1, angulo2)

# Mostrar el resultado
print(f"El tercer ángulo es: {resultado}° grados")
