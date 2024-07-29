def main():
    # Tamanho da matriz
    size = 11

    # Inicializa-se a matriz com 0s
    matrix = []
    for i in range(size):
        matrix.append([0] * size)

    # 
    for i in range(size):
        matrix[i][i] = 2

    for i in range(size):
        matrix[size-i-1][i] = 3

    midStart = int(size / 3)
    midEnd = size - midStart
    for i in range(midStart, midEnd):
        for j in range(midStart, midEnd):
            matrix[i][j] = 1

    center =  int(size / 2)
    matrix[center][center] = 4

    printMatrix(matrix)

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            cell = str(matrix[i][j]).rjust(3)
            print(cell, end='')
        print()
    print()

main()