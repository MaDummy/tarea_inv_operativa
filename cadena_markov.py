import numpy as np


def valida_matriz_transicion(matriz):
    """
    Valida que cada fila de la matriz de transición sume 1.
    """
    return np.allclose(np.sum(matriz, axis=1), 1)

def crea_coeficientes(matriz):
    """
    Ajusta la matriz para encontrar la distribución estacionaria.
    """
    for i in range(len(matriz)):
        matriz[i][i] -= 1
    matriz = np.vstack([matriz, np.ones(len(matriz))])
    return matriz

def calcula_prob_estacionaria(coeficientes):
    """
    Resuelve el sistema de ecuaciones para encontrar la distribución estacionaria.
    """
    A = np.array(coeficientes)
    b = np.zeros(len(A))
    b[-1] = 1  # La suma de las probabilidades estacionarias debe ser 1.
    try:
        x = np.linalg.lstsq(A, b, rcond=None)[0]
        return x
    except np.linalg.LinAlgError as e:
        return f"No se pudo resolver el sistema: {e}"

def main():
    """
    Función principal del programa.
    """
    
    # Definir la matriz de transición
    matriz_transitoria = np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.10, 0.80],
        [0.70, 0.15, 0.15]
    ])

    dicc_servidores = {
        0: "Miraflores",
        1: "Isla Teja",
        2: "Puerto Montt"
    }
    
    print("Matriz de transición usada:")
    print(matriz_transitoria)
    
    # Validar la matriz de transición
    if not valida_matriz_transicion(matriz_transitoria):
        print("Error: Una o más de las filas de distribución de probabilidad no suman 1.")
        return
    
    # Calcular la distribución estacionaria
    coeficientes = crea_coeficientes(matriz_transitoria.T)
    dist_estacionaria = calcula_prob_estacionaria(coeficientes)
    
    if isinstance(dist_estacionaria, str):
        print(dist_estacionaria)  # Mostrar el error si no se pudo resolver el sistema
        return
    
    # Mostrar resultados
    print("Distribución estacionaria calculada:")
    print(dist_estacionaria)
    print(f"El servidor con mayor probabilidad estacionaria es {dicc_servidores[np.argmax(dist_estacionaria)]}.")

if __name__ == "__main__":
    main()
