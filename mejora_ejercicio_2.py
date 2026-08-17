import threading
import time

def sumar_numeros(nombre, resultados, condicion, num_hilos, hilos_completados):
    """
    Función que suma números del 1 al 5.
    """
    total = sum(range(1, 6))
    time.sleep(1)  # Simular trabajo
    
    with condicion:
        resultados.append(f"{nombre} sumó: {total}")
        hilos_completados[0] += 1
        print(f"DEBUG: {nombre} completó su suma. Total: {hilos_completados[0]}/{num_hilos}")
        condicion.notify_all()

def crear_y_ejecutar_hilos(num_hilos=2):
    """
    Crea y ejecuta los hilos dinámicamente.
    """
    condicion = threading.Condition()
    resultados = []
    hilos_completados = [0]  # Usamos lista para mutabilidad
    
    # Crear hilos
    hilos = []
    for i in range(1, num_hilos + 1):
        hilo = threading.Thread(
            target=sumar_numeros,
            args=(f"Hilo {i}", resultados, condicion, num_hilos, hilos_completados)
        )
        hilos.append(hilo)
        hilo.start()
    
    # Esperar y mostrar resultados
    with condicion:
        condicion.wait_for(lambda: hilos_completados[0] == num_hilos)
        print("\n=== RESULTADOS FINALES ===")
        for resultado in resultados:
            print(resultado)
        print("¡Todos los hilos han completado su tarea!")
    
    # Esperar a que todos terminen
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    crear_y_ejecutar_hilos(3)