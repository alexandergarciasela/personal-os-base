# personal-os: una carpeta que guarda tu contexto para Claude

Aquí escribes quién eres, con quién trabajas y qué pasa con tus productos. Claude lee esos archivos cuando se los das y con eso prepara, resume y propone. Las tres rutinas ("archiva esto", "prepárame", "cierra el día") están descritas en `CLAUDE.md`. La carpeta no consulta tu calendario ni cambia tus herramientas sola.

## Empieza en diez minutos

1. Descarga una copia limpia (botón "Code", "Download ZIP") y llámala `personal-os`. No la mezcles con otra carpeta.
2. Llena `me.md`: rol, cómo trabajar contigo, una meta y un mensaje tuyo real.
3. Elige ahí dónde viven tus pendientes. Si es `abiertos.md`, escribe uno. Si usas una herramienta (Linear, Todoist, Notion), anota su nombre y enlace en `me.md` y borra `abiertos.md`.
4. En Claude Code: abre la carpeta. En claude.ai: crea un proyecto, pega `CLAUDE.md` en las instrucciones y sube `me.md` y `abiertos.md` a los archivos del proyecto. Omite `private/`.
5. Pregunta: `¿qué tengo abierto? dime de dónde lo sacaste`.

Funciona si usa tu pendiente y pide lo que no puede leer. Si dice que consultó una herramienta, pídele la fuente.

## Guarda antes de cambiar de chat

En Claude Code, revisa los archivos que cambió. En claude.ai, Claude no escribe archivos: te da la ruta y el contenido completo; tú lo guardas en la carpeta y reemplazas la copia anterior del proyecto. Si cambia `CLAUDE.md`, vuelve a pegarlo en las instrucciones. Una respuesta en el chat no actualiza nada.

## Prepara una conversación

Completa una persona en `people.md` y un producto en `projects/`. En `me.md`, anota con quién es tu próximo 1:1 y cuándo. Abre otro chat y pide: `prepárame para mi próximo 1:1`. `TALLER.md` lleva la práctica completa en cuatro paradas.

## Qué nunca va aquí

Contraseñas, claves ni tokens, tampoco en `private/`. Datos de otras personas sin su permiso. En el taller, material ficticio o anonimizado. Lo crudo y lo confidencial solo cabe en `private/`, y el nombre de la carpeta no restringe el acceso: lee `private/README.md` antes de usarla. Tu copia es personal; lo público es solo esta base.

## Cómo crece

- Un archivo por producto mientras encuentres su estado y sus decisiones. Cuando necesite varios documentos, pásalo a una carpeta.
- Cuando una rutina repita un error, corrige su instrucción en `CLAUDE.md` ese mismo día.
- Cada semana: revisa fechas, estado y próximo 1:1, y respalda la carpeta en tu nube o en un repo privado. `private/` no entra en git; respáldala aparte.
- Conectores, un agente en la nube que lea la carpeta desde GitHub y rutinas como skills entran después, cuando la carpeta ya vive.
