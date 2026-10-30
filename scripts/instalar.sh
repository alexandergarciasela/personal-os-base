#!/bin/bash
# Una vez por carpeta, cuando decides usar git: inicia el repo si falta, activa el chequeo de tres reglas
# antes de cada commit y crea trabajo/. Las rutinas ya vienen en .claude/skills/ y no necesitan instalación.
# Mac y Linux: Terminal. Windows: Git Bash (viene con git-scm.com) o WSL.
# Termina con "instalación completa" o con el error y su arreglo.
set -u
falla() { echo "error: $1 | arreglo: $2" >&2; exit 1; }
command -v git >/dev/null 2>&1 || falla "falta git" "Mac: xcode-select --install. Windows: git-scm.com (trae Git Bash)"
command -v python3 >/dev/null 2>&1 || falla "falta python3" "Mac: viene con xcode-select --install. Windows: python.org, marcando 'Add to PATH'"
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' || falla "python3 es anterior a 3.9" "instala Python 3.9 o más nuevo desde python.org"
AQUI="$(cd "$(dirname "$0")/.." && pwd)"
cd "$AQUI" || falla "no puedo entrar a $AQUI" "corre el script desde dentro de la carpeta"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  RAIZ="$(git rev-parse --show-toplevel)"
  [ "$RAIZ" = "$AQUI" ] || falla "esta carpeta está dentro de otro repo de git ($RAIZ)" "sácala a su propia carpeta, por ejemplo ~/personal-os, y vuelve a correr"
else
  git init -q -b main . 2>/dev/null || { git init -q . && git checkout -q -b main 2>/dev/null; }
  echo "git iniciado en $AQUI (rama main)"
fi
chmod +x .githooks/pre-commit scripts/instalar.sh scripts/revisar.py 2>/dev/null || true
ACTUAL="$(git config --get core.hooksPath || true)"
if [ -n "$ACTUAL" ] && [ "$ACTUAL" != ".githooks" ]; then
  falla "esta carpeta ya usa otros hooks ($ACTUAL)" "si quieres los de la base, corre: git config core.hooksPath .githooks"
fi
git config core.hooksPath .githooks || falla "no pude activar el chequeo" "corre a mano: git config core.hooksPath .githooks"
echo "chequeo antes de cada commit activo (.githooks/pre-commit)"
mkdir -p trabajo || falla "no pude crear trabajo/" "revisa los permisos de la carpeta"
python3 -I scripts/revisar.py full || falla "el chequeo encontró problemas (arriba)" "arregla lo que dice cada línea y vuelve a correr"
echo "instalación completa. Siguiente: git add -A && git commit -m 'mi personal OS' y sube la carpeta a un repo privado."
