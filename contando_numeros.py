import threading
import time

# Funcion que va a ejecutar cada hilo

def contar_numeros(nombre, contador):
    for i in range(1,6):
        time.sleep(1) # Simula un trabajo que toma tiempo (1 segundo por numero)
        print(f"{nombre} está contando: {contador + i}")

# Creamos dos hilos:

hilo1 = threading.Thread(target=contar_numeros, args=("Hilo 1", 0))
hilo2 = threading.Thread(target=contar_numeros, args=("Hilo 2", 5))

# Iniciamos ambos hilos:

hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen

hilo1.join()
hilo2.join()
print("¡Contador completo!")