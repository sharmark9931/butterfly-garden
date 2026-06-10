# 🦋 Butterfly Garden

A delightful animated butterfly garden that runs right inside your terminal — built with pure Python and curses, no dependencies required.

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)

---

## ✨ Features

- 🦋 **Colourful butterflies** with flapping wing animation in day mode
- ✦ **Glowing fireflies** that drift through the night sky
- 🌸 **Flowers with stems** that lean left or right with the wind
- ⛈️ **Rain & thunder** effects with lightning bolts at random positions
- ☀️ 🌙 **Auto day/night cycle** — or force it with a keypress
- 🌿 **Three themes:** spring, summer, autumn
- Zero external dependencies — uses Python's built-in `curses` module

---

## 📦 Installation

### Option 1 — Direct install (recommended, works everywhere)

**macOS / Linux:**
```bash
# Download the script
curl -fsSL https://raw.githubusercontent.com/sharmark9931/butterfly-garden/main/butterfly.py \
  -o ~/.local/bin/butterfly

# Make it executable
chmod +x ~/.local/bin/butterfly

# Add ~/.local/bin to your PATH (if not already)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc   # zsh
# or
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # bash

# Reload your shell
source ~/.zshrc   # or source ~/.bashrc

# Run!
butterfly
```

> **Corporate / restricted network?** Just download `butterfly.py` from the [Releases page](https://github.com/sharmark9931/butterfly-garden/releases), then:
> ```bash
> mkdir -p ~/.local/bin
> cp /path/to/butterfly.py ~/.local/bin/butterfly
> chmod +x ~/.local/bin/butterfly
> ```

---

### Option 2 — Homebrew tap (macOS)

> ⚠️ Requires up-to-date Xcode Command Line Tools (`xcode-select --install`).

```bash
brew tap sharmark9931/butterfly-garden
brew install butterfly-garden
```

---

### Option 3 — Run directly with Python (no install)

```bash
# Clone the repo
git clone https://github.com/sharmark9931/butterfly-garden.git
cd butterfly-garden

# Run
python3 butterfly.py
```

---

## 🚀 Usage

```bash
butterfly                     # default: spring theme, 20 butterflies
butterfly --theme summer      # start with summer theme
butterfly --theme autumn      # start with autumn theme
butterfly --count 40          # start with 40 butterflies
butterfly --count 5 --theme summer
```

### Available themes

| Theme    | Flowers               |
|----------|-----------------------|
| `spring` | 🌸 🌼 🌷              |
| `summer` | 🌻 🌺 🌼              |
| `autumn` | 🍁 🍂 🌻              |

---

## ⌨️ Keyboard Controls

| Key         | Action                                              |
|-------------|-----------------------------------------------------|
| `d`         | Force **day** mode (butterflies + sun)              |
| `n`         | Force **night** mode (fireflies + moon)             |
| `b`         | Add a butterfly                                     |
| `↑`         | Add a butterfly (day) / Add a firefly (night)       |
| `↓`         | Remove a butterfly (day) / Remove a firefly (night) |
| `←` `→`     | Adjust wind direction and strength                  |
| `r`         | Toggle **rain & thunder**                           |
| `t`         | Cycle through themes (spring → summer → autumn)     |
| `q`         | Quit                                                |

---

## 🖥️ Requirements

- **Python 3.8+** (comes pre-installed on macOS and most Linux distros)
- A terminal with **colour support** (iTerm2, Terminal.app, GNOME Terminal, etc.)
- Minimum terminal size: **80 × 24**

Check your Python version:
```bash
python3 --version
```

---

## 🗂️ Project Structure

```
butterfly-garden/
├── butterfly.py          # The entire app — single file, no dependencies
├── install.sh            # Convenience installer script
├── setup.py              # pip package config
├── Formula/
│   └── butterfly-garden.rb   # Homebrew formula
├── LICENSE
└── README.md
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b my-feature`
3. Commit your changes: `git commit -m "Add cool feature"`
4. Push and open a Pull Request

---

## 📄 License

MIT © [Ravi Kumar Sharma](https://github.com/sharmark9931)
