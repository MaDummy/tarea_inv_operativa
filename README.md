# **Cálculo de Distribución Estacionaria de Cadenas de Markov**

Este programa calcula la distribución estacionaria de una cadena de Markov a partir de una matriz de transición. Escrito en Python, valida la matriz de transición proporcionada y resuelve el sistema para determinar la distribución estacionaria.

---

## **Requisitos**
1. **Python**: Versión 3.12.3 o superior.
2. **Librerías**:
   - `numpy` (instalable con `pip install numpy`).

---

## **Cómo Ejecutar el Programa**

### **1. Clonar o Descargar el Repositorio**
Descarga el archivo `cadena_markov.py` en tu máquina local.

### **2. Ejecutar el Programa**
Abre una terminal o línea de comandos, navega al directorio donde se encuentra el archivo y ejecuta:

```bash
python3 cadena_markov.py
```

### **3. Resultado Esperado**
El programa mostrará:
1. La matriz de transición utilizada.
2. La distribución estacionaria calculada.
3. El estado con mayor probabilidad estacionaria.


## **Ejemplo de Uso**

### **Entrada Predefinida**
El programa usa la siguiente matriz de transición por defecto:
```plaintext
[[0.80, 0.10, 0.10],
 [0.10, 0.10, 0.80],
 [0.70, 0.15, 0.15]]
```

### **Salida**
```plaintext
Matriz de transición usada:
[[0.8  0.1  0.1 ]
 [0.1  0.1  0.8 ]
 [0.7  0.15 0.15]]
Distribución estacionaria calculada:
[0.70491803 0.10928962 0.18579235]
El estado con mayor probabilidad estacionaria es el estado 0.
```