# crudo/: lo que pegaste tal cual

Transcripciones, correos, notas de voz pasadas a texto. `crudo/AAAA-MM-DD-tema.md`. Solo se agrega: nada aquí se edita, se mueve ni se borra. Si una síntesis salió mal, se vuelve a procesar desde el crudo. Las reglas de escritura no aplican aquí: el crudo se guarda como llegó.

Única excepción: retirar un secreto o un dato de un tercero que no debió entrar. Se hace con el sí, se anota en `decisiones/`, y si era una contraseña o un token, se cambia esa credencial ese mismo día. Con git, ese commit se hace así, para que el chequeo lo deje pasar y quede registrado:

```
REVISAR_RETIRO=1 git commit -m "retiro: qué se quitó y por qué"
```

Si el secreto ya se subió a GitHub o se pegó en un chat, cambiar la credencial es lo que protege; borrarlo del archivo no basta.

Antes de pegar algo de otra persona, pregúntate si tienes su permiso. En un taller, usa material ficticio o ya anonimizado.
