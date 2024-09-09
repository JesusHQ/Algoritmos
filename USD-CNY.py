# Función que convierte de dólares estadounidenses (USD) a yuanes chinos (CNY)
def convertir_usd_a_cny(usd):
    # Tasa de conversión: 1 USD = 6.75 CNY
    conversion_rate = 6.75

    # Convertir la cantidad de USD a CNY
    cny = usd * conversion_rate

    # Formatear el resultado a dos decimales y agregar la cadena 'Chinese Yuan'
    return f"{cny:.2f} Chinese Yuan"


# Ejemplo de prueba 1
ejemplo_1 = convertir_usd_a_cny(15)
# Ejemplo de prueba 2
ejemplo_2 = convertir_usd_a_cny(465)

# Mostramos los resultados de los ejemplos
print(ejemplo_1)  # '101.25 Chinese Yuan'
print(ejemplo_2)  # '3138.75 Chinese Yuan'