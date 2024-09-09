# Función que calcula el costo total de los mangos con la oferta "3 por 2"
def mango(cantidad, precio_por_mango):
    # Cada 3 mangos, pagas solo 2, así que calculamos cuántos mangos pagados hay
    pagados = (cantidad // 3) * 2 + (cantidad % 3)

    # Calculamos el costo total
    costo_total = pagados * precio_por_mango
    return costo_total


# Pedir al usuario la cantidad de mangos y el precio por mango
cantidad = int(input("Introduce la cantidad de mangos: "))
precio_por_mango = float(input("Introduce el precio por mango: "))

# Calcular el costo total
costo = mango(cantidad, precio_por_mango)

# Mostrar el resultado
print(f"El costo total es: ${costo:.2f}")