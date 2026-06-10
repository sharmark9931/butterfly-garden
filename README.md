# 🦋 Butterfly Garden

An animated butterfly garden that runs right in your terminal — built with Python and curses.

## Features

- 🦋 Colourful ASCII butterflies with flapping wing animation (day mode)
- ✦ Glowing fireflies that drift in the breeze (night mode)
- 🌸 Flowers with stems that lean in the wind
- ⛈️  Rain & thunder effects
- ☀️ / 🌙 Auto day/night cycle (or force with `d` / `n`)
- 🌿 Three themes: spring, summer, autumn

## Install via Homebrew

```bash
brew tap YOUR_GITHUB_USERNAME/butterfly-garden
brew install butterfly-garden
```

## Usage

```bash
butterfly                        # defaults: 20 butterflies, spring theme
butterfly --count 40             # start with 40 butterflies
butterfly --theme summer         # start in summer theme
```

## Keyboard Controls

| Key | Action |
|-----|--------|
| `d` | Force day mode |
| `n` | Force night mode |
| `b` | Add a butterfly |
| `↑` / `↓` | Add / remove butterfly (day) or firefly (night) |
| `←` / `→` | Change wind direction & strength |
| `r` | Toggle rain & thunder |
| `t` | Cycle through themes |
| `q` | Quit |

## Requirements

- Python 3.8+
- macOS or Linux terminal with colour support

## License

MIT
