# **Cálculo de Distribución Estacionaria de Cadenas de Markov**

Este programa calcula la distribución estacionaria de una cadena de Markov a partir de una matriz de transición. Escrito en Python, valida la matriz de transición proporcionada y resuelve el sistema para determinar la distribución estacionaria.

---

# **Planteamiento del problema**
La Universidad Austral de Chile cuenta con un sistema  distribuido de servidores ubicados  
en tres de sus principales campus: Miraflores, La Isla Teja y  Puerto Montt. Estos servidores  
gestionan las solicitudes de los usuarios en las diversas   plataformas digitales de la  
universidad, tales como su sitio web, sistema de matrícula y  otros servicios en línea.  
Para asegurar que la carga de trabajo se distribuye de manera  eficiente y que ninguno de  
los servidores se sobrecargue, se ha implementado un sistema de  
balanceo de carga.  

Servidor de Miraflores tiene un 80% de probabilidad de  conservar una solicitud, un 10%  
de enviarla al Servidor de La Isla Teja y un 10% de enviarla al  
Servidor de Puerto Montt.  

Servidor de La Isla Teja tiene un 10% de probabilidad de  conservar una solicitud, un 10% de  
enviarla al Servidor de Miraflores y un 80% de enviarla al  Servidor de Puerto Montt.  

Servidor de Puerto Montt tiene un 70% de probabilidad de  conservar una solicitud, un 15%  
de enviarla al Servidor de Miraflores y un 15% de enviarla al   Servidor de La Isla Teja.  

Matriz de transicion:  
| 0.80 0.10 0.10 |  
| 0.10 0.10 0.80 |  
| 0.70 0.15 0.15 |  

Pregunta:
¿Cuál es la distribución estacionaria del tráfico de  solicitudes entre los tres servidores?  


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
El programa no recibe ninguna entrada, sino que usa la siguiente matriz de transición por defecto:
```plaintext
[[0.80, 0.10, 0.10],
 [0.10, 0.10, 0.80],
 [0.70, 0.15, 0.15]]
```
En caso de querer editar la matriz, cambiarla desde el código fuente.

### **Salida**
```plaintext
Matriz de transición usada:
[[0.8  0.1  0.1 ]
 [0.1  0.1  0.8 ]
 [0.7  0.15 0.15]]
Distribución estacionaria calculada:
[0.70491803 0.10928962 0.18579235]
El servidor con mayor probabilidad estacionaria es Miraflores.
```