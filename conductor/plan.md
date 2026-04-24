# Documento de Planificación (Ejecución)

Este documento describe las fases para construir y desplegar el MVP de Pomodoro Rocks.

## Fase 1: Core y Base de Datos (Semanas 1-2)
**Objetivo:** Tener el motor de tiempo y la base de datos funcionando de forma invisible.
- Configurar proyecto, entorno virtual y SQLite.
- Desarrollar el `timer.py` (máquina de estados de 30m / 8m).
- Implementar los "Bloques Duros" fijos del usuario (Hijos y Almuerzo).
- Desarrollar el monitoreo de actividad con `pynput`.

## Fase 2: Interfaz de Usuario y System Tray (Semanas 3-4)
**Objetivo:** Interfaz gráfica operativa comunicándose con el Daemon.
- Crear el System Tray icon (`pystray`).
- Diseñar la ventana principal con `CustomTkinter` (Modo Oscuro, minimalista).
- Conectar la UI con el Daemon (vía base de datos WAL o sockets locales) para mostrar el reloj en tiempo real.
- Crear vista de Chat (maquetado).

## Fase 3: Inteligencia Artificial y Visión (Semanas 5-6)
**Objetivo:** Dotar a la aplicación de su "cerebro" y capacidad de adaptación.
- Implementar el enrutador de IA (`ai/router.py`) conectando Gemini, OpenAI y DeepSeek.
- Crear el prompt de sistema para generar los "Retos de Descanso de 8 min".
- Implementar procesamiento de imágenes (Vision) para que el chat entienda capturas de pantalla de calendarios.
- Crear las "Herramientas" (Function Calling) para que el LLM pueda agregar/modificar Tareas y Eventos en SQLite.

## Fase 4: Sincronización API y Polish (Semanas 7-8)
**Objetivo:** Producto listo para producción y uso personal intensivo.
- Integrar Google Calendar API y MS Teams Graph API (OAuth local).
- Afinar la lógica para que los pomodoros se recalculen matemáticamente según los eventos sincronizados.
- Pruebas de estrés: Dejar el PC encendido, suspenderlo, probar reinicios y recuperación de estado del Pomodoro.
- Empaquetado en `.exe` usando `PyInstaller` o `Auto-py-to-exe`.
