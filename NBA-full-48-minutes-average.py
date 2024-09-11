# Función que calcula la extrapolación de los puntos por juego en 48 minutos
def nba_extrap(ppg, mpg):
    # Si los minutos por juego son 0, retornamos 0
    if mpg == 0:
        return 0
    # Extrapolamos los puntos por juego a 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48
    # Redondeamos a la décima más cercana
    return round(extrapolated_ppg, 1)

# Pedimos los datos al usuario por consola
ppg = float(input("Introduce los puntos por juego (ppg): "))
mpg = float(input("Introduce los minutos por juego (mpg): "))

# Calculamos la extrapolación
extrapolacion = nba_extrap(ppg, mpg)

# Mostramos el resultado
print(f"La extrapolación de puntos por 48 minutos es de: {extrapolacion}")
