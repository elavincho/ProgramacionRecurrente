import threading
import time

def contar_numeros(nombre, inicio, fin):
    """
    Función que cuenta números desde 'inicio' hasta 'fin' (inclusive)
    con una pausa para simular trabajo.
    """
    for i in range(inicio, fin + 1):
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        print(f"{nombre} está contando: {i}")

def crear_hilos(configuraciones):
    """
    Crea y retorna una lista de hilos basada en una lista de configuraciones.
    
    Args:
        configuraciones: Lista de tuplas (nombre, inicio, fin)
    
    Returns:
        Lista de objetos Thread
    """
    hilos = []
    for nombre, inicio, fin in configuraciones:
        hilo = threading.Thread(target=contar_numeros, args=(nombre, inicio, fin))
        hilos.append(hilo)
    return hilos

def ejecutar_hilos(hilos):
    """
    Inicia todos los hilos y espera a que todos terminen.
    
    Args:
        hilos: Lista de objetos Thread
    """
    # Iniciar todos los hilos
    for hilo in hilos:
        hilo.start()
    
    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

def main():
    """
    Función principal que configura y ejecuta el programa.
    """
    # Configuración centralizada de los hilos
    configuraciones = [
        ("Hilo 1", 1, 5),    # Hilo 1: cuenta del 1 al 5
        ("Hilo 2", 6, 10),   # Hilo 2: cuenta del 6 al 10
    ]
    
    print("Iniciando contadores en paralelo...")
    print(f"Se crearán {len(configuraciones)} hilos\n")
    
    # Crear y ejecutar los hilos
    hilos = crear_hilos(configuraciones)
    ejecutar_hilos(hilos)
    
    print("\n¡Contador completo!")

if __name__ == "__main__":
    main()