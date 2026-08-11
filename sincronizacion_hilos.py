import threading
import time

# Variables compartidas
suma_hilo1 = 0
suma_hilo2 = 0
hilos_completados = 0
condicion = threading.Condition()

def sumar_numeros(nombre, hilo_id):
    """
    Función que suma números del 1 al 5 y guarda el resultado en una variable compartida.
    Cuando termina, notifica a la condición.
    """
    global suma_hilo1, suma_hilo2, hilos_completados
    
    # Calcular la suma
    suma = 0
    for i in range(1, 6):
        print(f"{nombre}: sumando {i}")
        time.sleep(1.5)  # Simular trabajo
        suma += i
    
    # Guardar el resultado en la variable correspondiente
    if hilo_id == 1:
        suma_hilo1 = suma
    else:
        suma_hilo2 = suma
    
    print(f"{nombre}: terminó de sumar, resultado = {suma}")
    
    # Sincronización: adquirir el lock de la condición
    with condicion:
        global hilos_completados
        hilos_completados += 1
        print(f"{nombre}: hilos completados = {hilos_completados}")
        
        # Si ambos hilos han terminado, notificar
        if hilos_completados == 2:
            print("Ambos hilos han terminado. Despertando al hilo principal...")
            condicion.notify()

def hilo_principal():
    """
    Función que espera a que ambos hilos terminen y luego muestra los resultados.
    """
    global hilos_completados
    
    with condicion:
        # Esperar hasta que ambos hilos hayan terminado
        while hilos_completados < 2:
            print("Hilo principal: esperando a que los hilos terminen...")
            condicion.wait()
        
        # Mostrar los resultados
        print("\n=== RESULTADOS FINALES ===")
        print(f"Suma del Hilo 1: {suma_hilo1}")
        print(f"Suma del Hilo 2: {suma_hilo2}")
        print(f"Suma total: {suma_hilo1 + suma_hilo2}")
        print("¡Proceso completado!")

# Crear los hilos
hilo1 = threading.Thread(target=sumar_numeros, args=("Hilo 1", 1))
hilo2 = threading.Thread(target=sumar_numeros, args=("Hilo 2", 2))
hilo_principal_thread = threading.Thread(target=hilo_principal)

# Iniciar los hilos
print("Iniciando programa...")
hilo_principal_thread.start()
hilo1.start()
hilo2.start()

# Esperar a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo_principal_thread.join()

print("¡Programa finalizado!")



# Explicación del código:
# Variables compartidas:

# suma_hilo1 y suma_hilo2: almacenan los resultados de cada hilo.

# hilos_completados: contador de cuántos hilos han terminado.

# condicion: objeto Condition para sincronización.

# Función sumar_numeros:

# Cada hilo suma números del 1 al 5.

# Simula trabajo con time.sleep(1.5).

# Guarda su resultado en la variable correspondiente.

# Al terminar, adquiere el lock de la condición, incrementa el contador de hilos completados y si ambos hilos han terminado (hilos_completados == 2), notifica al hilo principal.

# Función hilo_principal:

# Espera usando condicion.wait() hasta que ambos hilos hayan terminado.

# Cuando recibe la notificación, muestra los resultados de ambos hilos.

# Flujo de ejecución:

# El hilo principal se inicia primero y entra en espera.

# Los dos hilos de suma se inician y ejecutan concurrentemente.

# Cuando ambos terminan, el hilo principal es notificado y muestra los resultados.

# Posible salida:
# text
# Iniciando programa...
# Hilo principal: esperando a que los hilos terminen...
# Hilo 1: sumando 1
# Hilo 2: sumando 1
# Hilo 1: sumando 2
# Hilo 2: sumando 2
# Hilo 1: sumando 3
# Hilo 2: sumando 3
# Hilo 1: sumando 4
# Hilo 2: sumando 4
# Hilo 1: sumando 5
# Hilo 2: sumando 5
# Hilo 1: terminó de sumar, resultado = 15
# Hilo 1: hilos completados = 1
# Hilo 2: terminó de sumar, resultado = 15
# Hilo 2: hilos completados = 2
# Ambos hilos han terminado. Despertando al hilo principal...

# === RESULTADOS FINALES ===
# Suma del Hilo 1: 15
# Suma del Hilo 2: 15
# Suma total: 30
# ¡Proceso completado!
# ¡Programa finalizado!
# Nota importante: La sincronización garantiza que los resultados solo se impriman cuando ambos hilos hayan completado su tarea, lo que demuestra el concepto de sincronización de hilos usando variables de condición.

