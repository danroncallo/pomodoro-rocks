# Documento de Conceptualización: Pomodoro Rocks (LLM Assistant)

## 1. Visión General
Una aplicación de escritorio para Windows, orientada a la productividad y la salud, que actúa como un asistente inteligente (LLM). Supera a los temporizadores tradicionales al leer dinámicamente la agenda del usuario (vía APIs de calendario o capturas de pantalla) y orquestar sesiones de Pomodoro (30 min trabajo / 8 min descanso) adaptadas a su rutina diaria.

## 2. Problema a Resolver
El sedentarismo, la fatiga visual y la desorganización causados por horarios rígidos o, paradójicamente, por la falta de ellos. Los temporizadores estáticos no entienden que el usuario tiene reuniones o compromisos inamovibles (ej. recoger a los hijos, almorzar), lo que provoca que las herramientas de productividad terminen siendo ignoradas o apagadas.

## 3. Propuesta de Valor
Un "Agente" Pomodoro invisible pero siempre presente. Conoce el horario, previene el agotamiento mediante rutinas dinámicas generadas por IA (hidratación, movilidad), y reprograma los bloques de trabajo automáticamente si detecta una nueva reunión o un cambio en el calendario.

## 4. Características Principales (Core Features)
- **Monitoreo Continuo:** Se inicia con el sistema operativo y detecta la actividad de la PC.
- **Rutina Fija Integrada:** Respeta los bloques duros del usuario (11:30 AM hijo, 12:14 PM hija, 1:00 PM almuerzo).
- **Pomodoros de 38 Minutos:** 30 minutos de enfoque absoluto y 8 minutos de recuperación activa.
- **Salud Dinámica (Generada por LLM):** En cada descanso, la IA propone ejercicios cortos, estiramientos, y recordatorios de hidratación para evitar la monotonía.
- **Interacción Multimodal:** Chatbot con soporte de visión para enviar "pantallazos" de la semana, o conexión vía OAuth (Google/Teams).
- **Autonomía:** Si el usuario no define tareas a las 7:00 u 8:00 AM, pero hay actividad en el teclado/mouse, el sistema asume el inicio de jornada y arranca los ciclos por defecto.
