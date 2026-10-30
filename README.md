# personal-os: una carpeta que guarda tu contexto para Claude

Aquí escribes quién eres, con quién trabajas y qué pasa con tus productos. Claude lee esos archivos cuando se los das y con eso prepara, resume y propone. Las tres rutinas ("archiva esto", "prepárame", "cierra el día") están descritas en `CLAUDE.md`; `EMPIEZA.md` te entrevista para llenar la carpeta la primera vez. La carpeta no consulta tu calendario ni cambia tus herramientas sola.

## Empieza con una entrevista

1. Descarga una copia limpia (botón "Code", "Download ZIP") y llámala `personal-os`. No la mezcles con otra carpeta.
2. En Claude Code, abre esa carpeta. En claude.ai, crea un proyecto, pega `CLAUDE.md` en sus instrucciones y sube `EMPIEZA.md`, `me.md`, `people.md` y `abiertos.md`. Omite `private/`.
3. Escribe: `Lee EMPIEZA.md y empieza la entrevista. Muéstrame los archivos antes de guardarlos`.
4. Contesta una pregunta por turno. Puedes decir "por confirmar" o "ahora no". En el taller, material ficticio o anonimizado.
5. Revisa los archivos que Claude proponga y di que sí. Si usas una herramienta de pendientes, las tareas siguen ahí; en `me.md` queda su nombre y enlace.

En el taller: 0 a 5 abrir la copia; 5 a 20 preguntas 1 a 5; 20 a 35 preguntas 6 a 8; 35 a 40 comprobar que quedó guardado; 40 a 50 la prueba en otro chat. Son hitos, no tiempos por pregunta.

## Guarda antes de cambiar de chat

En Claude Code, revisa los archivos que cambió. En claude.ai, Claude no escribe archivos: te da la ruta y el contenido completo; tú lo guardas en la carpeta y reemplazas la copia anterior del proyecto, también cada archivo nuevo de `projects/`. Al final reemplaza `EMPIEZA.md` y confirma "guardado y actualizado". Si cambia `CLAUDE.md`, vuelve a pegarlo en las instrucciones. Para retomar: `Lee EMPIEZA.md y sigamos`; solo recupera el avance que quedó guardado.

## Comprueba la preparación en otro chat

Abre otro chat en la misma carpeta o en el proyecto actualizado y pide: `prepárame para mi próximo 1:1`. Debe identificar a la persona y el producto, usar la decisión guardada y citar sus fuentes. Si no puede leer tu herramienta de pendientes, pega una copia actual cuando la pida. Si falla, corrige el archivo que toca y repite.

Esta semana: `archiva esto` con una conversación real, y revisa dónde quedaron decisiones y acciones. Después `cierra el día`: solo cierra lo que confirmes.

## Qué nunca va aquí

Contraseñas, claves ni tokens, tampoco en `private/`. Datos de otras personas sin su permiso. En el taller, material ficticio o anonimizado. Lo crudo y lo confidencial solo cabe en `private/`, y el nombre de la carpeta no restringe el acceso: lee `private/README.md` antes de usarla. Tu copia es personal; lo público es solo esta base.

## Cómo crece

- Un archivo por producto mientras encuentres su estado y sus decisiones. Cuando necesite varios documentos, pásalo a una carpeta.
- Cuando una rutina repita un error, corrige su instrucción en `CLAUDE.md` ese mismo día.
- Cada semana: revisa fechas, estado y próximo 1:1, y respalda la carpeta en tu nube o en un repo privado. `private/` no entra en git; respáldala aparte.
- Conectores, un agente en la nube que lea la carpeta desde GitHub y rutinas como skills entran después, cuando la carpeta ya vive.
