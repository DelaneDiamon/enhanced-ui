#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$PROJECT_ROOT/ssl"
STAGE_DIR="$PROJECT_ROOT/pack_ssl"

if [ -n "${MODS_DIR:-}" ]; then
  TARGET_MODS_DIR="$MODS_DIR"
elif [ -d "$PROJECT_ROOT/game_mods" ]; then
  TARGET_MODS_DIR="$PROJECT_ROOT/game_mods"
else
  TARGET_MODS_DIR="$PROJECT_ROOT/mods"
fi

ZIP_NAME="enhanced_ui.zip"
PAK_NAME="enhanced_ui.pak"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 command not found. Install Python 3 and retry." >&2
  exit 1
fi

if [ ! -d "$SRC_DIR" ]; then
  echo "Error: expected mod contents at $SRC_DIR." >&2
  exit 1
fi

rm -rf "$STAGE_DIR"
mkdir -p "$STAGE_DIR"
mkdir -p "$TARGET_MODS_DIR"

# Keep archive root at ssl/ as required by the game's mod loader.
cp -a "$SRC_DIR" "$STAGE_DIR/"

trap 'rm -rf "$STAGE_DIR"' EXIT

export STAGE_DIR TARGET_MODS_DIR ZIP_NAME PAK_NAME
python3 <<'PY'
import os
import zipfile

stage_dir = os.environ["STAGE_DIR"]
mods_dir = os.environ["TARGET_MODS_DIR"]
zip_name = os.environ["ZIP_NAME"]
pak_name = os.environ["PAK_NAME"]

zip_path = os.path.join(mods_dir, zip_name)
pak_path = os.path.join(mods_dir, pak_name)
ssl_root = os.path.join(stage_dir, "ssl")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(ssl_root):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, stage_dir)
            zf.write(full_path, arcname)

os.replace(zip_path, pak_path)
PY

echo "Built pak: $TARGET_MODS_DIR/$PAK_NAME"
