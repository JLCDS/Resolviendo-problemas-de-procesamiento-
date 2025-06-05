import threading
import random
import time

# Definición de recursos limitados
recursos = {
    "osciloscopio": 2,
    "generador_funciones": 1,
    "sala_experimentacion": 1
}

# Seguimiento de recursos en uso
reservas_activas = {
    "osciloscopio": 0,
    "generador_funciones": 0,
    "sala_experimentacion": 0
}

# Lock para evitar condiciones de carrera
lock = threading.Lock()

# Registro de tiempos de espera
tiempos_espera = {}

# Recursos reservados por cada estudiante
reservas_por_estudiante = {}

# Función principal que ejecuta el comportamiento de un estudiante
def estudiante(nombre):
    print(f"{nombre} intentando reservar...")
    tiempos_espera[nombre] = []
    reservas_por_estudiante[nombre] = []

    # El orden alfabético evita interbloqueos (acceso ordenado)
    recursos_solicitados = sorted(random.sample(list(recursos.keys()), k=2))

    for recurso in recursos_solicitados:
        inicio_espera = time.time()

        # Sección crítica protegida por lock
        while True:
            with lock:
                # Verifica disponibilidad del recurso
                if reservas_activas[recurso] < recursos[recurso]:
                    reservas_activas[recurso] += 1
                    reservas_por_estudiante[nombre].append(recurso)
                    break  # Sale del bucle si reservó el recurso
            time.sleep(0.05)

        fin_espera = time.time()
        tiempo_espera = fin_espera - inicio_espera
        tiempos_espera[nombre].append((recurso, tiempo_espera))
        print(f"{nombre} reserva {recurso} después de esperar {tiempo_espera:.2f}s")

    # Simula uso del recurso
    time.sleep(random.uniform(1, 2))

    # Libera cada recurso también dentro de sección crítica
    for recurso in reservas_por_estudiante[nombre]:
        with lock:
            reservas_activas[recurso] -= 1
        print(f"{nombre} libera {recurso}")

# Crear los hilos
hilos = []
for i in range(6):
    t = threading.Thread(target=estudiante, args=(f"Estudiante-{i+1}",))
    hilos.append(t)

# Iniciar hilos escalonadamente
for h in hilos:
    h.start()
    time.sleep(0.05)

# Esperar a que todos los hilos finalicen
for h in hilos:
    h.join()

# Mostrar tiempos de espera por recurso y estudiante
print("\n Tiempos de espera por estudiante:")
esperas_totales = {}
for est, tiempos in tiempos_espera.items():
    print(f"\n{est}:")
    for recurso, tiempo in tiempos:
        print(f"  → {recurso}: {tiempo:.2f}s")
        if recurso not in esperas_totales:
            esperas_totales[recurso] = []
        esperas_totales[recurso].append(tiempo)

# Mostrar promedios por recurso
print("\n Promedio de espera por recurso (con soluciones):")
for recurso, lista in esperas_totales.items():
    promedio = sum(lista) / len(lista)
    print(f"{recurso}: {promedio:.2f}s")
