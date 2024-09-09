# Función que redondea un número a dos decimales
def redondear_a_dos_decimales(numero):
    # Usamos la función round() para redondear a dos decimales
    return round(numero, 2)

# Pedir al usuario un número por consola
numero = float(input("Introduce un número: "))

# Redondear el número a dos decimales
numero_redondeado = redondear_a_dos_decimales(numero)

# Mostrar el resultado
print(f"El número redondeado a dos decimales es: {numero_redondeado}")
