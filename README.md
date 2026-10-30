# personal-os: la base

Un personal OS es una carpeta de archivos de texto que una IA lee antes de responderte. Ahí viven tu memoria (quién eres, qué llevas, con quién trabajas, qué decidiste), tus reglas (lo que la IA nunca hace) y tus rutinas (lo que haces dos veces, escrito una vez). Claude es el cerebro; la carpeta es tuya y no se muda con el modelo.

Esta base es el punto de partida del taller. No es un producto: es la carpeta mínima que crece contigo. Los archivos los conservas tú y se los das a la IA; lo que no actualices, la IA no lo sabe.

## Arranca en 10 minutos

1. Descarga esta carpeta (botón "Code", "Download ZIP") y ponla en tu escritorio con el nombre `personal-os`.
2. Llena `me.md` (seis líneas). En `metas.md`, un resultado del trimestre y un foco de la semana bastan. En `abiertos.md`, tres pendientes reales.
3. Ábrela con Claude Code. O en claude.ai: crea un proyecto y sube a sus archivos todo lo que hay en la carpeta (`AGENTS.md`, `me.md`, `metas.md`, `abiertos.md`, `contexto/`, `plantillas/` y los cuatro `SKILL.md` de `.claude/skills/`; esa carpeta está oculta: en Mac, Cmd+Shift+punto la muestra); pega `AGENTS.md` también en las instrucciones.
4. Pregunta: `¿qué tengo abierto?`

Funciona si contesta con lo que escribiste y pregunta lo que no sabe. Prueba de que persiste: cierra el chat, abre otro, pregunta lo mismo.

En claude.ai la IA no escribe archivos: te entrega el nombre y el contenido completo de cada archivo, tú lo guardas en la carpeta, borras la versión anterior del proyecto y subes la nueva. El resultado es el mismo; cambia quién guarda.

## Antes de pegar algo

- Sin contraseñas, tokens ni claves. La IA los quita y avisa, aunque le digas que sí.
- Datos de otras personas solo con su permiso. En un taller, material ficticio o ya anonimizado.
- Si algo entró por error: se retira (la única excepción a "crudo/ no se toca", ver `crudo/README.md`), se anota en `decisiones/`, se revisa si ya está en GitHub o en un chat, y si era una credencial, se cambia ese mismo día.

## Qué hay en cada lugar

| Dónde | Qué | Cuándo entra |
|---|---|---|
| `AGENTS.md` | Las reglas de la casa para cualquier IA. `CLAUDE.md` solo apunta aquí. | Hoy |
| `me.md` | Quién eres, cómo quieres que te hable, un mensaje tuyo real para el tono. | Hoy |
| `metas.md` | Resultados del trimestre y foco de la semana. | Hoy |
| `abiertos.md` | Tus pendientes, si no tienes una herramienta de pendientes. Un solo lugar, nunca dos. | Hoy |
| `.claude/skills/` | Las cuatro rutinas, una carpeta por rutina con su `SKILL.md`. Cualquier IA las lee ahí. | Hoy |
| `contexto/` | Lo que no cambia: dónde vive cada cosa, tu empresa o tus clientes, tu glosario. | Esta semana |
| `personas/` | Una carpeta por persona con la que trabajas: cómo le gusta que le escriban, qué acordaron. | Con la primera reunión |
| `reuniones/` | Una síntesis por reunión: qué se decidió, qué quedó abierto. | Con la primera reunión |
| `decisiones/` | Una decisión por archivo, con fecha y estado. Tu decision log. | Con la primera decisión |
| `crudo/` | Lo que pegas tal cual: transcripciones, correos, notas de voz. No se edita. | Con la primera transcripción |
| `plantillas/` | Un molde por tipo de archivo. | Cuando la IA cree uno |
| `trabajo/` | Borradores. Fuera de git. | Siempre |
| `scripts/` | Un chequeo de tres reglas antes de cada commit, cuando uses git. | Cuando uses git |

## Las cuatro rutinas

| Dices | Rutina | Qué hace |
|---|---|---|
| `¿qué tengo hoy?` | `prep-dia` | Cruza tus metas, tus pendientes y tu calendario si está conectado, y deja una lista corta. |
| `archiva esto` | `archiva-reunion` | Guarda el crudo, escribe la síntesis, propone decisiones y pendientes en un bloque, y deja el seguimiento listo para pegar. |
| `prepárame` | `preparame` | Antes de hablar con alguien: qué le debes, qué te debe, qué preguntar. |
| `cierra el día` | `cierre-del-dia` | Qué quedó hecho, qué se mueve y hasta tres prioridades para mañana. |

Una rutina corre cuando la llamas. La carpeta no hace nada sola.

## Respaldo desde hoy

Copia la carpeta a tu nube (iCloud, Drive, OneDrive) o guarda un ZIP cada semana. Si pierdes la computadora, no pierdes el contexto. Cuando quieras versiones: `bash scripts/instalar.sh` inicia git y activa el chequeo de tres reglas antes de cada commit (crudo intocable, sin secretos, sin guion largo). Súbela a un repo privado, nunca público.

## Cómo crece

- Una regla nueva entra cuando el mismo error pasa dos veces, y va en el lugar más estrecho que lo evita: un paso de una rutina antes que `AGENTS.md`.
- Una carpeta nueva entra cuando te estorba no tenerla, no antes.
- Un conector (MCP) entra cuando una rutina lo necesite: calendario para `prep-dia`, tu herramienta de pendientes para `cierre-del-dia`. Lo que la IA lee de un conector no se copia crudo a la carpeta.

## Ampliaciones, cuando la carpeta ya vive

- **Permisos.** `.claude/settings.json` pide confirmación antes de hacer commit o push y antes de que un conector cree, actualice, borre, envíe o publique algo (por el nombre de la acción; un conector con nombres raros puede escaparse). Niega el push forzado. Tú envías.
- **Siempre encendido.** Un agente en la nube (GrokBot u otro) con su propia cuenta y permisos lee la última copia que subiste a GitHub y te habla por el celular: brief de la mañana, alertas con contexto, borradores con tu voz. No depende de tu computadora.
- **Otros repos.** Desde la carpeta se detona trabajo en otros repos con todo tu contexto: un fix, un deck, un doc. El cerebro ordena; los otros repos ejecutan.

## Qué nunca va aquí

Contraseñas, tokens, datos de clientes que no te pertenecen, transcripciones de otros sin su permiso, y pendientes en dos lugares.
