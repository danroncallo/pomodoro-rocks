# Documento de Diseño: Pomodoro Rocks

## 1. Arquitectura del Sistema
El sistema utilizará una **Arquitectura de Proceso Dual** para garantizar robustez:
1. **Core Daemon (Background Service):** Un proceso en Python (sin interfaz gráfica) que corre constantemente. Maneja la lógica del tiempo, chequea actividad del sistema operativo (`pynput` / llamadas a la API de Windows), coordina las llamadas al LLM y guarda datos en SQLite.
2. **Frontend UI:** Una aplicación gráfica desarrollada en `CustomTkinter`. Se minimiza a la bandeja del sistema (System Tray). Funciona como cliente del Daemon, mostrando el temporizador, el chat y las listas de tareas.

## 2. Diseño de Interfaz (UI/UX)
- **Minimalismo y Modernidad:** Tonos oscuros (Dark Mode por defecto), bordes redondeados, tipografía sans-serif limpia (ej. Segoe UI, Roboto).
- **No Invasivo:** Notificaciones sutiles integradas con Windows 11. El panel principal solo se abre a petición o durante los 8 minutos de descanso activo.
- **Vistas Principales:**
  1. *Dashboard/Timer:* Círculo o barra de progreso minimalista.
  2. *Chat AI:* Interfaz conversacional estilo ChatGPT para subir pantallazos o pedir ajustes.
  3. *Agenda/Tareas:* Lista de tareas sincronizada con el LLM.

## 3. Integración de Inteligencia Artificial (LLMs)
- **Enrutador de Modelos (Model Router):** 
  - *Tier 1:* Gemini (Pro/Flash) preferido por su rapidez y bajo costo en visión (pantallazos).
  - *Tier 2:* OpenAI (GPT-4o/mini) o DeepSeek como fallbacks para procesamiento lógico complejo o fallas de red.
- **Function Calling (Agentic Behavior):** La IA tendrá acceso a herramientas internas (ej. `update_task`, `pause_pomodoro`, `schedule_meeting`) para que el chat altere directamente la base de datos del usuario sin intervención manual.

## 4. Generación de Descansos
Durante el minuto 29 del ciclo, el Daemon hace un llamado asíncrono al LLM solicitando un "Micro-Reto de 8 minutos". El prompt de sistema asegura variedad (ej. *Día 1, Pomodoro 3: Haz 15 sentadillas y mira por la ventana a 20 metros*).
