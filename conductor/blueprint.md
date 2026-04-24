# Documento Blueprint Técnico

## 1. Tech Stack
- **Lenguaje:** Python 3.11+
- **Frontend:** `customtkinter`, `pystray` (System Tray), `Pillow` (manejo de imágenes).
- **Backend/Daemon:** `asyncio`, `fastapi` (para comunicación IPC local) o `multiprocessing` con colas.
- **Base de Datos:** `sqlite3` + `SQLAlchemy` (ORM) o `Peewee`.
- **Integraciones OS:** `pynput` (actividad), `win11toast` (notificaciones).
- **IA/APIs:** `google-generativeai`, `openai`, `requests` (DeepSeek), Google Calendar API, MS Graph API (Teams).

## 2. Estructura del Proyecto
```text
pomodoro_rocks/
│
├── core/                   # Daemon y lógica de negocio
│   ├── timer.py            # Máquina de estados del Pomodoro
│   ├── activity.py         # Monitoreo de inactividad/actividad
│   └── scheduler.py        # Adaptador de la rutina fija
│
├── ai/                     # Capa de LLM y Agentes
│   ├── router.py           # Gestor de fallbacks y API keys
│   ├── vision.py           # Procesamiento de pantallazos
│   └── tools.py            # Funciones expuestas al LLM (Function Calling)
│
├── database/               # Modelos y acceso a datos
│   ├── models.py           # Task, PomodoroSession, Event, BreakRoutine
│   └── crud.py
│
├── ui/                     # Frontend en CustomTkinter
│   ├── main_window.py
│   ├── tray_icon.py
│   └── chat_widget.py
│
├── main.py                 # Entrypoint (Lanza Daemon y/o UI)
└── requirements.txt
```

## 3. Modelos de Datos (SQLite)
- **Task:** id, title, status, created_at, scheduled_for
- **Event:** id, source (Google/Teams/Vision), start_time, end_time, is_hard_block (booleano para hijos/almuerzo).
- **Session:** id, start_time, end_time, type (work/break), status (completed/interrupted), ai_break_prompt.
- **Config:** Claves API, preferencias de inicio, horas fijas.

## 4. Comunicación Inter-Procesos (IPC)
El Daemon levantará un servidor local ultra-ligero (ej. `localhost:8080`) o usará un archivo de base de datos SQLite con Write-Ahead Logging (WAL). La UI de CustomTkinter consultará periódicamente el estado (`polling` cada 1 segundo) o escuchará un socket para actualizar el reloj sin bloquearse.
