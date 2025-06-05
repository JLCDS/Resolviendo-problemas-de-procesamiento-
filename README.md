# Resolviendo problemas de procesamiento

Este proyecto aborda la simulación de un sistema de reserva de recursos limitados en un laboratorio utilizando programación concurrente en Python. Se implementan dos versiones del sistema: una con problemas de sincronización y otra con soluciones para evitar condiciones de carrera e interbloqueos.

## Archivos del proyecto

- **Punto2Problema.py**: Contiene la implementación inicial del sistema de reserva, donde los estudiantes intentan reservar recursos sin mecanismos de sincronización adecuados. Esto puede generar problemas como condiciones de carrera e interbloqueos.
- **Punto2Solucion.py**: Contiene la implementación mejorada del sistema de reserva, utilizando un `Lock` para proteger las secciones críticas y un orden alfabético para evitar interbloqueos.
- **README.md**: Este archivo describe el proyecto y su estructura.

## Descripción del sistema

El laboratorio cuenta con tres tipos de recursos limitados:
- Osciloscopios (2 disponibles)
- Generadores de funciones (1 disponible)
- Sala de experimentación (1 disponible)

Cada estudiante intenta reservar dos recursos aleatorios y los utiliza durante un tiempo simulado. Al finalizar, libera los recursos para que otros estudiantes puedan utilizarlos.

### Problemas abordados
1. **Condiciones de carrera**: Ocurren cuando múltiples hilos acceden y modifican los mismos datos de forma concurrente sin sincronización.
2. **Interbloqueos**: Ocurren cuando varios hilos se bloquean mutuamente al intentar acceder a recursos que ya están reservados por otros.

### Soluciones implementadas
- Uso de un `Lock` para proteger las secciones críticas y evitar condiciones de carrera.
- Orden alfabético en la reserva de recursos para evitar interbloqueos.

## Ejecución del proyecto

1. **Versión con problemas**:
   Ejecuta el archivo `Punto2Problema.py` para observar los problemas de sincronización y los tiempos de espera de los estudiantes.

   ```bash
   python Punto2Problema.py
   ```

2. **Versión sin problemas**:
   Ejecuta el archivo `Punto2Solucion.py` para ver el funcionamiento del sistema con las soluciones implementadas.

   ```bash
   python Punto2Solucion.py
   ```

## Observaciones

- Asegúrate de tener instalado Python 3.x en tu sistema.
- Es recomendable ejecutar las pruebas en un entorno aislado para evitar interferencias con otras aplicaciones.
- Los tiempos de espera y los resultados pueden variar en cada ejecución debido a la naturaleza concurrente del programa.