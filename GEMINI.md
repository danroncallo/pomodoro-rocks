# Pomodoro Rocks - Contexto del Proyecto

## Visión General
**Pomodoro Rocks** es un asistente de productividad y salud proactivo, diseñado como una aplicación de escritorio para Windows utilizando Python. A diferencia de los temporizadores tradicionales, este sistema funciona como un agente LLM que adapta dinámicamente las sesiones de Pomodoro (30m enfoque / 8m descanso) basándose en la agenda real del usuario, analizada a través de APIs (Google/Teams) o visión artificial (capturas de pantalla).

## Especificaciones de Diseño
- **Arquitectura:** Proceso Dual (Daemon en segundo plano + Interfaz CustomTkinter).
- **Interfaz:** Minimalista, moderna, no invasiva (System Tray) y en modo oscuro.
- **Inteligencia Artificial:** Rotación de APIs (Gemini, OpenAI, DeepSeek) con sistema de fallback.
- **Salud:** Rutinas dinámicas generadas por IA durante los descansos para combatir el sedentarismo (movilidad, hidratación, fatiga visual).

## Estructura Técnica y Directorios
La aplicación se organiza de forma modular para separar la lógica de negocio, la interfaz y la integración con IA:

```text
pomodoro_rocks/
├── core/                   # MOTOR PRINCIPAL (DAEMON)
│   ├── timer.py            # Máquina de estados: Work (30m) / Break (8m)
│   ├── activity.py         # Monitor de mouse/teclado (pynput)
│   ├── scheduler.py        # Orquestador de rutina diaria y bloques duros
│   └── observer.py         # Sistema de eventos para comunicación interna
├── ai/                     # CEREBRO LLM
│   ├── router.py           # Gestor de fallbacks (Gemini -> OpenAI -> DeepSeek)
│   ├── vision.py           # OCR y análisis de capturas de pantalla de calendarios
│   ├── agents.py           # Lógica de planificación proactiva
│   └── tools.py            # Function Calling (ej: add_task, reschedule_day)
├── database/               # PERSISTENCIA (SQLite)
│   ├── models.py           # Esquemas (Tasks, Events, Sessions, Config)
│   ├── crud.py             # Operaciones de lectura/escritura
│   └── database.py         # Configuración de la conexión (WAL mode)
├── ui/                     # INTERFAZ GRÁFICA (CustomTkinter)
│   ├── app.py              # Ventana principal y navegación
│   ├── components/         # Widgets reutilizables (Timer, Chat, TaskList)
│   ├── styles/             # Temas personalizados y assets visuales
│   └── tray.py             # Integración con la bandeja del sistema (pystray)
├── api/                    # INTEGRACIONES EXTERNAS
│   ├── google_calendar.py  # Autenticación OAuth y lectura de eventos
│   └── teams_graph.py      # Conexión con Microsoft Graph API
├── utils/                  # UTILIDADES
│   ├── logger.py           # Sistema de logs para depuración del daemon
│   └── config_manager.py   # Cifrado de API Keys y gestión de .env
├── main.py                 # Punto de entrada (Orquesta Daemon + UI)
└── requirements.txt        # Dependencias del proyecto
```

## Horario y Reglas de Negocio
El sistema respeta bloques inamovibles ("Hard Breaks"):
- **Inicio:** 8:00 AM (o detección de actividad entre 7:00-8:00 AM).
- **Recoger Hijo:** 11:30 AM - 11:45 AM.
- **Recoger Hija:** 12:14 PM - 12:29 PM.
- **Almuerzo:** 1:00 PM - 2:00 PM.
- **Cierre:** 5:00 PM / 6:00 PM (Dinámico).
- **Ciclo:** 30 minutos de trabajo / 8 minutos de descanso activo.

## Documentación de Referencia
Los detalles de implementación se encuentran en la carpeta `/conductor`:
- `conceptualization.md`: Visión y propuesta de valor.
- `design.md`: Arquitectura y UI/UX.
- `blueprint.md`: Stack técnico y estructura de archivos.
- `user-stories.md`: Requerimientos detallados.
- `plan.md`: Fases de ejecución.

## Firma y Estándar
**Firma:** jaguardluz
**Estándar:** Jaguar v3.1 (Excelencia Silicon Valley 2025-2026).
