import threading
import random
import time

# Recursos limitados en el laboratorio
recursos = {
    "osciloscopio": 2,
    "generador_funciones": 1,
    "sala_experimentacion": 1
}

# Contador de recursos actualmente en uso
reservas_activas = {
    "osciloscopio": 0,
    "generador_funciones": 0,
    "sala_experimentacion": 0
}

# Diccionario que registra qué recursos ha reservado cada estudiante
reservas_por_estudiante = {}

# Diccionario que registra el tiempo de espera por recurso para cada estudiante
tiempos_espera = {}

# Función que representa a un estudiante intentando reservar recursos
def estudiante(nombre):
    global reservas_activas, reservas_por_estudiante

    print(f"{nombre} intentando reservar...")
    tiempos_espera[nombre] = []

    # Elige dos recursos aleatorios
    orden = random.sample(list(recursos.keys()), k=2)
    reservas_por_estudiante[nombre] = []

    for recurso in orden:
        inicio_espera = time.time()  # Marca de tiempo inicial

        # Espera activa mientras el recurso no esté disponible
        while reservas_activas[recurso] >= recursos[recurso]:
            time.sleep(0.05)

        fin_espera = time.time()  # Marca de tiempo cuando obtiene el recurso
        tiempo_total = fin_espera - inicio_espera
        tiempos_espera[nombre].append((recurso, tiempo_total))

        print(f"{nombre} reserva {recurso} después de esperar {tiempo_total:.2f}s")
        reservas_activas[recurso] += 1
        reservas_por_estudiante[nombre].append(recurso)

    # Simula uso de los recursos durante 1–2 segundos
    time.sleep(random.uniform(1, 2))

    # Libera los recursos reservados
    for recurso in reservas_por_estudiante[nombre]:
        reservas_activas[recurso] -= 1
        print(f"{nombre} libera {recurso}")

# Crear e iniciar los hilos (estudiantes)
hilos = []
for i in range(6):
    t = threading.Thread(target=estudiante, args=(f"Estudiante-{i+1}",))
    hilos.append(t)

# Ejecutar cada hilo con una pequeña espera entre ellos
for h in hilos:
    h.start()
    time.sleep(0.05)

# Esperar a que todos los hilos terminen
for h in hilos:
    h.join()

# Mostrar los tiempos de espera de cada estudiante por recurso
print("\n Tiempos de espera por estudiante:")
esperas_totales = {}
for est, tiempos in tiempos_espera.items():
    print(f"\n{est}:")
    for recurso, tiempo in tiempos:
        print(f"  → {recurso}: {tiempo:.2f}s")
        if recurso not in esperas_totales:
            esperas_totales[recurso] = []
        esperas_totales[recurso].append(tiempo)

# Calcular y mostrar el promedio de espera por recurso
print("\n Promedio de espera por recurso:")
for recurso, lista in esperas_totales.items():
    promedio = sum(lista) / len(lista)
    print(f"{recurso}: {promedio:.2f}s")
