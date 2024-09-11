# Función que calcula la presión total usando la fórmula dada
def calcular_presion_total(m1, M1, m2, M2, V, T_C):
    # Constante de los gases ideales
    R = 0.082  # dm^3 · atm · K^−1 · mol^−1

    # Convertir la temperatura de °C a Kelvin
    T_K = T_C + 273.15

    # Calcular los moles de cada gas
    moles_gas1 = m1 / M1
    moles_gas2 = m2 / M2

    # Calcular la presión total
    P_total = (moles_gas1 + moles_gas2) * R * T_K / V

    return P_total


# Ejemplo de prueba con valores arbitrarios
m1 = 10  # masa del gas 1 en gramos
M1 = 18  # masa molar del gas 1 en g/mol
m2 = 20  # masa del gas 2 en gramos
M2 = 32  # masa molar del gas 2 en g/mol
V = 5  # volumen en dm^3
T_C = 25  # temperatura en grados Celsius

# Calcular la presión total
presion_total = calcular_presion_total(m1, M1, m2, M2, V, T_C)
print(presion_total)