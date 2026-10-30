---
name: preparame
description: Prepara una conversación cuando la persona dice "prepárame", "prepárame para X" o "voy a hablar con X". Lee el perfil de la persona, los acuerdos vigentes, los pendientes con ella y la última reunión, y entrega qué le debe, qué sigue y qué preguntar. Solo lee; si falta el perfil, lo propone y lo crea solo con el sí.
---

# Prepárame

Cuándo: "prepárame", "prepárame para X", "voy a hablar con X", "qué tengo con X".

## Pasos
1. Lee `personas/<nombre>/perfil.md`. Si no existe, pregunta una cosa a la vez: qué hace, cómo le gusta que le escriban, qué acordaron. Al final ofrece crear la carpeta, con el sí.
2. Lee la última síntesis en `reuniones/` donde aparezca, las decisiones vigentes que la toquen, y los pendientes abiertos con esa persona donde vivan (`abiertos.md` o la herramienta de `contexto/fuentes.md`).
3. Entrega en tres bloques cortos: qué le debes tú, qué te debe, qué preguntar hoy. Cierra con una línea de cómo le gusta que le hablen.
4. Si la persona pide un mensaje, redáctalo en su tono y en el idioma del destinatario, y déjalo listo para pegar.

## Nunca
- Enviar el mensaje. La persona lo pega.
- Inventar un acuerdo que no esté escrito.
- Poner juicios sobre la persona en el archivo: hechos, acuerdos y fechas.
