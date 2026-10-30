# El taller: de carpeta vacía a personal OS en 50 minutos

Cuatro paradas. En cada una escribes algo real tuyo y le haces una pregunta a Claude. El objetivo es que la carpeta exista, conteste y una rutina corra; no que quede perfecta.

Antes de empezar: ten abierto Claude Code o claude.ai con sesión iniciada. Hoy no abrimos cuentas ni depuramos logins. Si vas a pegar una reunión real, que sea tuya y sin datos de terceros; si no, usa esta: "Junta con Ana, hoy. Acordamos que yo le mando la propuesta el viernes y ella consigue el presupuesto antes del 15. Decidimos empezar por el piloto chico y no por el lanzamiento completo."

El ciclo es siempre el mismo: tú dictas o pegas, Claude consulta la carpeta, te propone un borrador, tú revisas y guardas o envías.

## Parada 1 (minutos 0 a 10): hazla tuya
1. Descarga esta carpeta al escritorio con el nombre `personal-os`.
2. Llena `me.md`: seis líneas. En `metas.md`, un resultado y un foco bastan. Tres pendientes reales en `abiertos.md`. Sin clientes, sin montos, sin tokens.
3. Abre la carpeta con Claude Code. O en claude.ai: proyecto nuevo, sube los archivos de la carpeta y pega `AGENTS.md` en las instrucciones.
4. Pregunta: `¿qué tengo abierto?`

Funciona si contesta con lo tuyo y pregunta lo que no sabe.

## Parada 2 (minutos 10 a 25): tu primera reunión
1. Pega una transcripción, o dicta en tres líneas lo que pasó en tu última reunión.
2. Di: `archiva esto`.
3. Revisa el bloque numerado que propone: el crudo, la síntesis, las decisiones, la carpeta de la persona, los pendientes. Di "todo" o "1 y 3". En claude.ai, guarda tú los archivos que te entrega y súbelos al proyecto.
4. Abre `reuniones/`, `decisiones/` y `personas/`. Esa es tu memoria creciendo.

## Parada 3 (minutos 25 a 40): dos rutinas sobre lo que acabas de archivar
1. Di: `prepárame para <la persona de la reunión>`. Lee lo que te debe, lo que le debes y qué preguntar.
2. Di: `cierra el día`. Contesta qué cerraste. Mira cómo cambia `abiertos.md` y el perfil de la persona.
3. Si ya tienes un conector (MCP) de calendario o correo activo, marca "sí" en `contexto/fuentes.md` y pregunta `¿qué tengo hoy?`. Si no, queda para esta semana: en claude.ai es Configuración, Conectores; en Claude Code, `/mcp`.

## Parada 4 (minutos 40 a 50): que persista
1. Cierra el chat. Abre otro. Pregunta `¿qué tengo abierto?`. Si contesta con lo de hoy, tu memoria ya no depende del chat.
2. Respalda: copia la carpeta a tu nube o guarda un ZIP. Si quieres versiones, `bash scripts/instalar.sh` y súbela a un repo privado.
3. Mira en pantalla las capas que siguen: permisos (tú envías), un agente siempre encendido que lee la carpeta desde GitHub, y otros repos que ejecutan con tu contexto. Hoy no se instalan.

## Esta semana
- Una rutina corre de verdad: una reunión archivada o un cierre del día.
- Un conector conectado, con sesión ya iniciada y en una tarde tranquila.
- La primera regla nueva nace cuando algo salga mal dos veces.
