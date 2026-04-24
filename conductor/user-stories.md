# Historias de Usuario

## Épica 1: Gestión Autónoma del Tiempo y Actividad
**US 1.1: Arranque con Windows**
- *Como* usuario, *quiero* que el asistente inicie silenciosamente cuando enciendo mi PC *para* no tener que recordar abrirlo.
- *Criterios de Aceptación:* Se agrega al registro de inicio de Windows. Aparece en el System Tray.

**US 1.2: Detección de Actividad**
- *Como* usuario, *quiero* que la app empiece a contar mi día a las 8:00 AM automáticamente si detecta que estoy usando el teclado o mouse, *para* que registre mi trabajo aunque olvide configurar mis tareas.
- *Criterios de Aceptación:* Si pasa la hora de inicio y hay inputs de hardware, el estado pasa a "Trabajando".

**US 1.3: Respeto de Bloques Duros**
- *Como* padre, *quiero* que el timer se pause o ajuste para nunca sonar entre 11:30-11:45 AM, 12:14-12:29 PM y 1:00-2:00 PM *para* poder atender a mis hijos y almorzar sin estrés.

## Épica 2: Integración de Horarios (Vision y API)
**US 2.1: Carga de Pantallazo**
- *Como* usuario, *quiero* pegar una captura de pantalla de mi calendario en el chat *para* que la IA bloquee mis horas de reuniones automáticamente.
- *Criterios de Aceptación:* La IA reconoce eventos, horarios y los inserta en la base de datos local.

**US 2.2: Sincronización Google/Teams**
- *Como* profesional, *quiero* conectar mis cuentas *para* que la app lea mi agenda diariamente sin que yo tenga que hacer nada.

## Épica 3: Asistente Conversacional y Salud
**US 3.1: Descansos Dinámicos**
- *Como* trabajador remoto, *quiero* que cada 30 minutos la app me proponga un ejercicio de 8 minutos generado por IA *para* cuidar mi salud física y visual.
- *Criterios de Aceptación:* Notificación push de Windows con la instrucción del ejercicio. Se abre una vista minimalista en la UI si el usuario hace clic.

**US 3.2: Modificación de Base de Datos vía Chat**
- *Como* usuario, *quiero* decirle a la IA "agrega hacer reporte a mis tareas de hoy" *para* que modifique la base de datos sin que yo navegue por menús.
