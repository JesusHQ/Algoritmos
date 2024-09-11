import math  # Importamos la librería math para usar la función ceil()

def convertir_a_aspecto_16_9(x, y):
    # Calculamos el nuevo ancho (X) para tener una relación de aspecto de 16:9
    # La fórmula es: nuevo_x = y * (16 / 9) para mantener la altura igual
    # Usamos math.ceil() para redondear el valor hacia arriba al entero más cercano
    nuevo_x = math.ceil(y * 16 / 9)

    # Retornamos el nuevo ancho con la misma altura original
    return nuevo_x, y
# Ejemplo de prueba: tenemos una imagen de 374x280 píxeles
ejemplo_x, ejemplo_y = 374, 280

# Llamamos a la función para obtener la nueva resolución con aspecto 16:9
nueva_resolucion = convertir_a_aspecto_16_9(ejemplo_x, ejemplo_y)

# Mostramos la nueva resolución en la consola
print(nueva_resolucion)