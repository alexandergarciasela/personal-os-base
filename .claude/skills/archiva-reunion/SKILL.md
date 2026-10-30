---
name: archiva-reunion
description: Procesa una reunión cuando la persona dice "archiva esto", "archiva la reunión con X" o pega una transcripción. Guarda el crudo, escribe la síntesis con la plantilla, propone decisiones, acuerdos por persona y pendientes en un solo bloque numerado, y deja el seguimiento listo para pegar. Nada se guarda sin el sí; nada se envía.
---

# Archiva una reunión

Cuándo: "archiva esto", "archiva la reunión con X", "procesa esta transcripción", o la persona pega una transcripción o dicta lo que pasó.

## Pasos
1. Antes de leer a fondo, revisa el texto pegado: si trae contraseñas, tokens o claves, dilo y quítalos del crudo antes de cualquier otra cosa. Si trae datos personales de terceros, pregunta si hay permiso; sin permiso, se resumen sin nombre.
2. Arma un solo bloque numerado con todo lo que propones guardar en la carpeta:
   1. El crudo tal cual (ya sin secretos) en `crudo/AAAA-MM-DD-tema.md`.
   2. La síntesis con `plantillas/reunion.md`: una línea de qué pasó, decisiones, cuántos pendientes salieron y dónde quedan, y el seguimiento en el tono de la persona.
   3. Una decisión por archivo en `decisiones/` con `plantillas/decision.md`. Si reemplaza a una vigente, incluye el cambio de estado de la vieja. Si contradice una vigente sin reemplazarla, dilo antes.
   4. La línea nueva de acuerdos en `personas/<nombre>/perfil.md` de cada persona de la reunión. Si no tiene carpeta, su creación va como un punto más del bloque.
   5. Los pendientes, en `abiertos.md` o en la herramienta que diga `contexto/fuentes.md`, una sola vez. Si a uno le falta dueño o fecha, pregunta; si la persona no lo sabe, se guarda con "por confirmar" en ese campo, nunca inventado.
3. Espera el sí por lote ("todo", "1 y 3"). Solo entonces se escribe. Sin acceso a archivos, entrega el contenido completo de cada archivo, para pegar.
4. El seguimiento queda listo para pegar. Enviarlo es otra orden, aparte: solo con "envíalo" sobre ese texto. Lo mismo para crear un pendiente en una herramienta externa.

## Nunca
- Guardar sin el sí; enviar sin "envíalo".
- Inventar un acuerdo, un dueño o una fecha que no se dijo.
- Citar textual a alguien fuera de la carpeta. El seguimiento se redacta nuevo, en paráfrasis.
- Guardar contraseñas, tokens o claves, aunque la persona diga que sí.
