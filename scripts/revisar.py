#!/usr/bin/env python3
"""Tres reglas antes de cada commit. Python 3.9 o más nuevo, sin instalar nada.

  python3 -I scripts/revisar.py staged   lo que está por entrar al commit (lo llama .githooks/pre-commit)
  python3 -I scripts/revisar.py full     toda la carpeta: archivos rastreados y nuevos no ignorados

Reglas:
  R1 crudo/ solo se agrega: nada ahí se modifica, mueve, cambia de tipo ni se borra (salvo crudo/README.md).
     Única excepción, para retirar un secreto o un dato de un tercero: REVISAR_RETIRO=1 git commit -m "retiro: qué y por qué".
     R2 y R3 siguen corriendo; el commit queda en el historial como prueba del retiro.
  R2 sin secretos: tokens, claves y contraseñas con forma conocida no entran. Es una detección parcial:
     no reemplaza el cuidado de no pegarlos.
  R3 sin guion largo en los .md (regla de escritura; no aplica a crudo/; quítala si no la quieres).

Si git falla, el chequeo falla: nunca aprueba en silencio.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SECRETOS = [
    (re.compile(r"sk-[A-Za-z0-9_\-]{20,}"), "clave con prefijo sk-"),
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"), "token de GitHub"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "token de GitHub"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"), "token de Slack"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "clave de AWS"),
    (re.compile(r"AIza[0-9A-Za-z_\-]{30,}"), "clave de Google"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "llave privada"),
    (re.compile(r"(?i)(password|contraseña|passwd|api[_\- ]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9/+_\-]{12,}"), "contraseña o clave en texto"),
]
GUION_LARGO = "—"
TEXTO = {".md", ".json", ".toml", ".txt", ".py", ".sh", ".yml", ".yaml", ".csv", ""}


class GitFallo(Exception):
    pass


def git(*args):
    try:
        r = subprocess.run(["git", "-c", "core.quotepath=false", *args], cwd=RAIZ, capture_output=True)
    except FileNotFoundError:
        raise GitFallo("falta git | arreglo: instálalo y vuelve a intentar")
    if r.returncode != 0:
        raise GitFallo("git " + " ".join(args) + " falló: " + r.stderr.decode("utf-8", "replace").strip())
    return r.stdout


def decodificar(crudo):
    if b"\x00" in crudo[:8000]:
        return None
    return crudo.decode("utf-8", "replace")


def archivos_staged():
    salida = git("diff", "--cached", "--name-status", "--diff-filter=ADMRT", "-M", "-z")
    partes = salida.split(b"\x00")
    filas = []
    i = 0
    while i < len(partes):
        estado = partes[i].decode("utf-8", "replace")
        if not estado:
            i += 1
            continue
        if estado[0] == "R":
            origen, destino = partes[i + 1].decode("utf-8", "replace"), partes[i + 2].decode("utf-8", "replace")
            filas.append(("R", destino, origen))
            i += 3
        else:
            filas.append((estado[0], partes[i + 1].decode("utf-8", "replace"), None))
            i += 2
    return filas


def contenido_staged(ruta):
    return decodificar(git("show", ":" + ruta))


def es_crudo(ruta):
    return ruta.startswith("crudo/") and ruta != "crudo/README.md"


def r1_crudo(filas):
    fallas = []
    if os.environ.get("REVISAR_RETIRO") == "1":
        tocados = [ruta for _, ruta, origen in filas if es_crudo(ruta) or (origen and es_crudo(origen))]
        if tocados:
            print("R1 omitido por retiro autorizado (REVISAR_RETIRO=1): " + ", ".join(tocados) + " | anótalo en decisiones/")
        return fallas
    for estado, ruta, origen in filas:
        if not (es_crudo(ruta) or (origen and es_crudo(origen))):
            continue
        if estado == "M":
            fallas.append(("R1", ruta, "se modificó un crudo", "quítalo del commit (git restore --staged) y deshaz el cambio (git checkout -- archivo); lo nuevo va en otro archivo"))
        elif estado == "D":
            fallas.append(("R1", ruta, "se borró un crudo", "recupéralo (git checkout -- archivo); crudo/ solo se agrega"))
        elif estado == "R":
            fallas.append(("R1", ruta, "se movió desde " + origen, "deja el original donde estaba"))
        elif estado == "T":
            fallas.append(("R1", ruta, "cambió de tipo", "deja el original como estaba"))
    return fallas


def r2_secretos(pares):
    fallas = []
    for ruta, texto in pares:
        for patron, que in SECRETOS:
            m = patron.search(texto)
            if m:
                linea = texto[: m.start()].count("\n") + 1
                fallas.append(("R2", ruta + ":" + str(linea), que, "quítalo del archivo y cambia esa credencial; los secretos van en un gestor de contraseñas, nunca aquí"))
                break
    return fallas


def r3_guion(pares):
    fallas = []
    for ruta, texto in pares:
        if not ruta.endswith(".md") or ruta.startswith("crudo/"):
            continue
        if GUION_LARGO in texto:
            linea = texto[: texto.index(GUION_LARGO)].count("\n") + 1
            fallas.append(("R3", ruta + ":" + str(linea), "guion largo", "cámbialo por coma, punto o dos puntos"))
    return fallas


def pares_full():
    salida = git("ls-files", "-z", "--cached", "--others", "--exclude-standard")
    pares = []
    for cruda in salida.split(b"\x00"):
        if not cruda:
            continue
        ruta = cruda.decode("utf-8", "replace")
        p = RAIZ / ruta
        if not p.is_file() or p.suffix not in TEXTO:
            continue
        texto = decodificar(p.read_bytes())
        if texto is not None:
            pares.append((ruta, texto))
    return pares


def correr(modo):
    try:
        if modo == "staged":
            filas = archivos_staged()
            fallas = r1_crudo(filas)
            pares = []
            for estado, ruta, _ in filas:
                if estado == "D":
                    continue
                texto = contenido_staged(ruta)
                if texto is not None:
                    pares.append((ruta, texto))
        else:
            fallas = []
            pares = pares_full()
    except GitFallo as e:
        print("revisar " + modo + ": no pude revisar | " + str(e))
        return 1
    fallas += r2_secretos(pares) + r3_guion(pares)
    for regla, ruta, que, arreglo in fallas:
        print(regla + " " + ruta + ": " + que + " | arreglo: " + arreglo)
    if fallas:
        print(str(len(fallas)) + " problema(s). El commit no entra hasta arreglarlos.")
        return 1
    print("revisar " + modo + ": todo en orden (" + str(len(pares)) + " archivos)")
    return 0


if __name__ == "__main__":
    if sys.version_info < (3, 9):
        print("revisar: necesita Python 3.9 o más nuevo | arreglo: instala Python desde python.org")
        sys.exit(1)
    modo = sys.argv[1] if len(sys.argv) > 1 else "staged"
    if modo not in {"staged", "full"}:
        print(__doc__)
        sys.exit(2)
    sys.exit(correr(modo))
