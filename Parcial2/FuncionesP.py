# Funcion para comprobar si la secuencia ingresada es mutante o no
def is_mutant(dna):
    def check_horizontal():
        for row in dna:
            for i in range(len(row) - 3):
                if row[i:i+4] == "AAAA" or row[i:i+4] == "TTTT" or row[i:i+4] == "CCCC" or row[i:i+4] == "GGGG":
                    return True
        return False

    def check_vertical():
        for i in range(len(dna[0])):
            column = "".join(row[i] for row in dna)
            for j in range(len(column) - 3):
                if column[j:j+4] == "AAAA" or column[j:j+4] == "TTTT" or column[j:j+4] == "CCCC" or column[j:j+4] == "GGGG":
                    return True
        return False

    def check_diagonals():
        for i in range(len(dna) - 3):
            for j in range(len(dna[0]) - 3):
                diagonal = "".join(dna[x][y] for x, y in zip(
                    range(i, i + 4), range(j, j + 4)))
                if diagonal == "AAAA" or diagonal == "TTTT" or diagonal == "CCCC" or diagonal == "GGGG":
                    return True
        return False

    return check_horizontal() or check_vertical() or check_diagonals()


# Funcion para verificar que la secuencia ingresada sea valida
def is_valid_dna(dna):
    valid_bases = set("ATCG")
    if not all(set(row).issubset(valid_bases) and len(row) == len(dna) for row in dna):
        return False
    return len(dna) == len(dna[0])


# Funcion para ingresar la secuencia de ADN por teclado
def input_dna_sequence():
    dna = []
    while True:
        print("Ingrese la secuencia de ADN (filas separadas por Enter, letras A, T, C, G):")
        try:
            for _ in range(6):
                # Convierte en mayusculas para evitar errores y trabajar mejor
                row = input().strip().upper()
                dna.append(row)
            if is_valid_dna(dna):
                return dna
            else:
                print("La matriz de ADN ingresada no es válida. Verifique que sea una matriz 6x6 y contenga solo bases válidas (A, T, C, G).")
                dna = []  # Reiniciar la matriz si es invalida
        except KeyboardInterrupt:
            print("Entrada interrumpida. Saliendo.")
            exit(1)


# Funcion principal del programa
def main():
    dna_sequence = input_dna_sequence()
    result = is_mutant(dna_sequence)

    if result:
        print("El humano es mutante.")
    else:
        print("El humano no es mutante.")


if __name__ == "__main__":
    main()
