import numpy as np

"""
La Universidad Austral de Chile cuenta con un sistema distribuido de servidores ubicados
en tres de sus principales campus: Miraflores, La Isla Teja y Puerto Montt. Estos servidores
gestionan las solicitudes de los usuarios en las diversas plataformas digitales de la
universidad, tales como su sitio web, sistema de matrícula y otros servicios en línea.
Para asegurar que la carga de trabajo se distribuye de manera eficiente y que ninguno de
los servidores se sobrecargue, se ha implementado un sistema de balanceo de carga.

Servidor de Miraflores tiene un 80% de probabilidad de conservar una solicitud, un 10%
de enviarla al Servidor de La Isla Teja y un 10% de enviarla al Servidor de Puerto Montt.

Servidor de La Isla Teja tiene un 10% de probabilidad de conservar una solicitud, un 10% de
enviarla al Servidor de Miraflores y un 80% de enviarla al Servidor de Puerto Montt.

Servidor de Puerto Montt tiene un 70% de probabilidad de conservar una solicitud, un 15%
de enviarla al Servidor de Miraflores y un 15% de enviarla al Servidor de La Isla Teja.

matriz de transicion:
| 0.80 0.10 0.10 |
| 0.10 0.10 0.80 |
| 0.70 0.15 0.15 |

Pregunta:
¿Cuál es la distribución estacionaria del tráfico de solicitudes entre los tres servidores?
"""


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
    
    # Solicitar la matriz de transición
    matriz_transitoria = np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.10, 0.80],
        [0.70, 0.15, 0.15]
    ])
    
    print("Matriz de transición usada:")
    print(matriz_transitoria)
    
    # Validar la matriz de transición
    if not valida_matriz_transicion(matriz_transitoria):
        print("Error: Las filas de la matriz de transición no suman 1.")
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
    print(f"El estado con mayor probabilidad estacionaria es el estado {np.argmax(dist_estacionaria)}.")

if __name__ == "__main__":
    main()
