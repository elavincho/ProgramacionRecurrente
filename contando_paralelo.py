import threading
import time

def contar_numeros(nombre, inicio, fin):
    """
    Función que cuenta números desde 'inicio' hasta 'fin' (inclusive)
    y los imprime con una pequeña pausa para simular trabajo.
    """
    for i in range(inicio, fin + 1):
        time.sleep(0.5)  # Pausa de 0.5 segundos para simular trabajo
        print(f"{nombre}: {i}")

# Crear los dos hilos
hilo1 = threading.Thread(target=contar_numeros, args=("Hilo 1", 1, 5))
hilo2 = threading.Thread(target=contar_numeros, args=("Hilo 2", 6, 10))

# Iniciar ambos hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("¡Contador completo!")


# Explicación del código:
# Función contar_numeros:

# Recibe un nombre para identificar el hilo, un número de inicio y un número de fin.

# Itera desde inicio hasta fin (inclusive).

# Usa time.sleep(0.5) para simular que el hilo está haciendo trabajo, lo que permite que ambos hilos se ejecuten de forma concurrente.

# Imprime el número junto con el nombre del hilo.

# Creación de hilos:

# hilo1 cuenta del 1 al 5.

# hilo2 cuenta del 6 al 10.

# Inicio y espera:

# start() inicia la ejecución de cada hilo.

# join() hace que el programa principal espere a que cada hilo termine antes de continuar.

# Posible salida (el orden puede variar):
# text
# Hilo 1: 1
# Hilo 2: 6
# Hilo 1: 2
# Hilo 2: 7
# Hilo 1: 3
# Hilo 2: 8
# Hilo 1: 4
# Hilo 2: 9
# Hilo 1: 5
# Hilo 2: 10
# ¡Contador completo!
# Nota: El orden de impresión puede variar cada vez que ejecutes el programa porque los hilos compiten por el tiempo de CPU, y el sistema operativo decide cuándo ejecutar cada uno. Esto demuestra el concepto de concurrencia.