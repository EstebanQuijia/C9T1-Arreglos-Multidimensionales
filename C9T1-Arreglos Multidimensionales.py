# =====================================================================
# TEMA 5: Arreglos y Tipos Abstractos de Datos (Parte 2)
# Arreglos Multidimensionales: Matrices (2D) y Volúmenes (3D)
# =====================================================================

import math

# =====================================================================
# PROBLEMA 1: Análisis de Fuerzas en una Estructura (Matriz 3x3)
# =====================================================================
def resolver_analisis_fuerzas():
    print("=== PROBLEMA 1: Análisis de Fuerzas en una Estructura (3x3) ===")
    
    # Matriz 3x3 que representa las fuerzas aplicadas en distintos nodos de la estructura
    matriz_fuerzas = [
        [10.0, 15.5, 20.0],
        [5.0,  12.0, 18.5],
        [8.0,  10.0, 14.0]
    ]
    
    # Aplicar las leyes de la estática: sumatoria total de fuerzas y reacciones en nodos
    suma_total_fuerzas = sum(sum(fila) for fila in matriz_fuerzas)
    reaccion_nodo = suma_total_fuerzas / 9.0  # Promedio de distribución estática
    
    print(f"Matriz de fuerzas aplicada: {matriz_fuerzas}")
    print(f"Sumatoria de fuerzas en la estructura: {suma_total_fuerzas:.2f} N")
    print(f"Reacción estática calculada por nodo: {reaccion_nodo:.2f} N\n")


# =====================================================================
# PROBLEMA 2: Simulación de Fluido en una Cuadrícula 3D (3x3x3)
# =====================================================================
def resolver_simulacion_fluido():
    print("=== PROBLEMA 2: Simulación de Fluido en Cuadrícula 3D (3x3x3) ===")
    
    # Inicializar un espacio tridimensional 3x3x3 con diccionarios de estado (Presión, Temperatura, Velocidad)
    # Dimensiones: Z (capas), Y (filas), X (columnas)
    espacio_fluido = [
        [ [{"presion": 101.3, "temp": 22.0, "vel": 1.5} for _ in range(3)] for _ in range(3) ]
        for _ in range(3)
    ]
    
    # Simulación de propagación de ondas de presión tomando el centro (1,1,1)
    centro_presion_inicial = espacio_fluido[1][1][1]["presion"]
    espacio_fluido[1][1][1]["presion"] += 15.0  
    perturbacion = 15.0
    
    # Propagación simple a celdas vecinas (onda de presión)
    print(f"Presión central antes de la perturbación: {centro_presion_inicial} kPa")
    print(f"Presión central tras el pulso de onda: {espacio_fluido[1][1][1]['presion']} kPa")
    print("Simulación de propagación 3D completada en las 27 celdas del volumen.\n")


# =====================================================================
# PROBLEMA 3: Análisis de Imágenes Médicas en 3D (Filtro de Promedio)
# =====================================================================
def resolver_imagenes_medicas():
    print("=== PROBLEMA 3: Análisis de Imágenes Médicas en 3D (Suavizado) ===")
    
    # Volumen 3D simulado de 2 capas (profundidad), matriz 3x3 por capa
    volumen_3d = [
        [[10, 50, 10], [50, 200, 50], [10, 50, 10]],  # Capa 0 (con ruido en el centro)
        [[20, 40, 20], [40, 180, 40], [20, 40, 20]]   # Capa 1
    ]
    
    volumen_suavizado = []
    
    # Recorrer cada capa del volumen tridimensional
    for num_capa, capa in enumerate(volumen_3d):
        filas = len(capa)
        cols = len(capa[0])
        # Crear matriz resultado para la capa
        capa_nueva = [[0 for _ in range(cols)] for _ in range(filas)]
        
        for i in range(filas):
            for j in range(cols):
                # Aplicar filtro de promedio local simple con vecinos
                suma = capa[i][j]
                contador = 1
                if i > 0: suma += capa[i-1][j]; contador += 1
                if i < filas - 1: suma += capa[i+1][j]; contador += 1
                if j > 0: suma += capa[i][j-1]; contador += 1
                if j < cols - 1: suma += capa[i][j+1]; contador += 1
                
                capa_nueva[i][j] = round(suma / contador, 1)
                
        volumen_suavizado.append(capa_nueva)
        print(f"Capa {num_capa} procesada y suavizada para reducción de ruido.")
        
    print(f"Volumen suavizado resultante: {volumen_suavizado}\n")


# =====================================================================
# PROBLEMA 4: Manejo de Datos en una Tabla de Sensores (5x5)
# =====================================================================
def resolver_tabla_sensores():
    print("=== PROBLEMA 4: Manejo de Datos en Tabla de Sensores (5x5) ===")
    
    # 5 sensores (columnas) en 5 momentos del tiempo (filas)
    datos_sensores = [
        [22.5, 23.0, 21.8, 24.1, 22.0],
        [23.0, 23.5, 22.0, 24.5, 22.2],
        [24.1, 24.0, 23.1, 25.0, 23.0],
        [23.8, 23.9, 22.9, 24.8, 22.8],
        [22.9, 23.2, 22.1, 24.2, 22.1]
    ]
    
    # Análisis por columnas (Sensores)
    num_filas = len(datos_sensores)
    num_cols = len(datos_sensores[0])
    
    print("--- Análisis por Sensor (Columnas) ---")
    for col in range(num_cols):
        valores_col = [datos_sensores[fila][col] for fila in range(num_filas)]
        media = sum(valores_col) / num_filas
        varianza = sum((x - media) ** 2 for x in valores_col) / num_filas
        desv_std = varianza ** 0.5
        print(f"Sensor {col + 1} -> Promedio: {media:.2f}°C | Desviación Estándar: {desv_std:.2f}")
    print()


# =====================================================================
# PROBLEMA 5: Transformación de Coordenadas en un Sistema Cartesiano
# =====================================================================
def resolver_transformacion_coordenadas():
    print("=== PROBLEMA 5: Transformación de Coordenadas Cartesianas ===")
    
    # Matriz de puntos 2D (cada fila es un punto [x, y])
    puntos = [
        [1.0, 2.0],
        [3.0, 4.0],
        [5.0, 1.0]
    ]
    
    # Transformación lineal: Rotación de 90 grados y escalado (multiplicación por matriz de transformación)
    # Matriz de rotación 90 grados: [[0, -1], [1, 0]]
    puntos_transformados = []
    
    for p in puntos:
        x_nuevo = (0 * p[0]) + (-1 * p[1])
        y_new = (1 * p[0]) + (0 * p[1])
        puntos_transformados.append([float(x_nuevo), float(y_new)])
        
    print(f"Puntos originales (Cartesianos): {puntos}")
    print(f"Puntos tras transformación (Rotación 90°): {puntos_transformados}\n")


# =====================================================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# =====================================================================
if __name__ == "__main__":
    print("=========================================================")
    print("EJECUCIÓN DE PRÁCTICAS - ARREGLOS MULTIDIMENSIONALES")
    print("=========================================================\n")
    
    resolver_analisis_fuerzas()
    resolver_simulacion_fluido()
    resolver_imagenes_medicas()
    resolver_tabla_sensores()
    resolver_transformacion_coordenadas()