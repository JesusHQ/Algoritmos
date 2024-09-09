def calculate_pet_years(human_years):
    # Calcular años del gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calcular años del perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Pedir al usuario la cantidad de años humanos
human_years = int(input("Introduce la cantidad de años humanos: "))

# Calcular los años del gato y del perro
result = calculate_pet_years(human_years)

# Imprimir el resultado
print(f"Human Years: {result[0]}, Cat Years: {result[1]}, Dog Years: {result[2]}")
