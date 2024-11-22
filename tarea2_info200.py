import numpy as np


def crea_coeficientes(matriz:list) -> list:
    for i in range(3):
        matriz[i][i] -= 1
    matriz = np.vstack([matriz, np.array([1, 1, 1])])
    print(matriz)
    return matriz


def calcula_prob_estacionaria(coeficientes: list) -> list:
    A = np.array(coeficientes)
    b = np.array([0, 0, 0, 1])

    try:
        x = np.linalg.lstsq(A, b, rcond=None)[0]
        return x
    except np.linalg.LinAlgError as e:
        return f"No se pudo resolver el sistema: {e}"


def main():
    matriz_transitoria = np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.10, 0.80],
        [0.70, 0.15, 0.15]
    ])

    coeficientes = crea_coeficientes(matriz_transitoria.T)

    dist_estacionaria = calcula_prob_estacionaria(coeficientes)

    print(np.argmax(dist_estacionaria))

if __name__ == "__main__":
    main()