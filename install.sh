#!/bin/bash
# One-line installer — no Homebrew, no CLT required.
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/sharmark9931/butterfly-garden/main/install.sh | bash

set -e

INSTALL_DIR="$HOME/.local/bin"
SCRIPT_URL="https://raw.githubusercontent.com/sharmark9931/butterfly-garden/main/butterfly.py"
DEST="$INSTALL_DIR/butterfly"

# Ensure python3 is available
if ! command -v python3 &>/dev/null; then
  echo "Error: python3 not found. Install Python 3 first." >&2
  exit 1
fi

mkdir -p "$INSTALL_DIR"
curl -fsSL "$SCRIPT_URL" -o "$DEST"
chmod +x "$DEST"

echo "✅ Installed butterfly to $DEST"

# Warn if ~/.local/bin is not on PATH
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
  echo ""
  echo "⚠️  Add this line to your ~/.zshrc or ~/.bash_profile:"
  echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
  echo "Then restart your terminal and run: butterfly"
else
  echo "Run it now with: butterfly"
fi
