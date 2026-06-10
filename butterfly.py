#!/usr/bin/env python3
"""
Butterfly garden terminal animation.
Keys: [d]ay  [n]ight  [b]utterfly+  [r]ain  [t]heme  [← →]wind  [q]uit
"""

import curses
import random
import math
import time
import argparse

# ── Wing-animation frames ────────────────────────────────────────────────────
# ASCII chars so curses color-pairs actually colour them (emoji ignore pairs).
# Body = *, wings change shape each frame.
WING_FRAMES = [
    "^*^",   # wings high
    "-*-",   # wings level
    "v*v",   # wings low
]

# ── Themes ───────────────────────────────────────────────────────────────────
THEMES = {
    "spring": {"flowers": ["🌸", "🌼", "🌷"]},
    "summer": {"flowers": ["🌻", "🌺", "🌼"]},
    "autumn": {"flowers": ["🍁", "🍂", "🌻"]},
}

# ── Celestial art ────────────────────────────────────────────────────────────
SUN_ART  = [r" \|/ ", "-(☀)-", r" /|\ "]
MOON_ART = [" (🌙)", "  )  ", "     "]


# ── Entities ─────────────────────────────────────────────────────────────────

class Butterfly:
    """Smooth wandering movement + independent flap animation."""

    def __init__(self, w, h):
        self.x  = random.uniform(4, w - 6)
        self.y  = random.uniform(2, h - 10)
        # velocity
        angle   = random.uniform(0, 2 * math.pi)
        speed   = random.uniform(0.1, 0.35)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed * 0.5
        # target velocity for smooth steering
        self.tvx = self.vx
        self.tvy = self.vy
        self.wander_cd = random.randint(20, 60)
        # colour: 1–7, bold so the terminal actually shows distinct hues
        self.color = random.randint(1, 7)
        # flap: each butterfly has its own phase & rate
        self.flap  = random.uniform(0, math.pi * 2)
        self.frate = random.uniform(0.18, 0.40)   # radians per tick
        self.frame = 0

    def update(self, wind, w, h):
        # advance wing-flap frame
        self.flap += self.frate
        # map continuous phase → 0/1/2/1/0/… for smooth up→mid→down→mid cycle
        t = (math.sin(self.flap) + 1) / 2      # 0..1
        self.frame = int(t * 2.99)              # 0, 1 or 2

        # wander: periodically choose a new target direction
        self.wander_cd -= 1
        if self.wander_cd <= 0:
            angle = random.uniform(0, 2 * math.pi)
            spd   = random.uniform(0.1, 0.4)
            self.tvx = math.cos(angle) * spd
            self.tvy = math.sin(angle) * spd * 0.5
            self.wander_cd = random.randint(20, 60)

        # smooth steering (lerp toward target)
        self.vx += (self.tvx - self.vx) * 0.06
        self.vy += (self.tvy - self.vy) * 0.06

        # flutter: tiny rapid bob layered on top
        flutter = math.sin(self.flap * 3) * 0.10

        self.x += self.vx + wind
        self.y += self.vy + flutter

        # wrap horizontally
        self.x %= max(w - 5, 1)
        # bounce vertically
        if self.y < 2:
            self.y = 2;      self.vy =  abs(self.vy)
        if self.y > h - 8:
            self.y = h - 8;  self.vy = -abs(self.vy)


class Firefly:
    def __init__(self, w, h):
        self.x     = random.uniform(1, w - 2)
        self.y     = random.uniform(2, max(3, h // 2))
        self.phase = random.uniform(0, math.pi * 2)
        spd = random.uniform(0.05, 0.20)
        ang = random.uniform(0, 2 * math.pi)
        self.dx = math.cos(ang) * spd
        self.dy = math.sin(ang) * spd * 0.4

    def update(self, w, h, wind=0.0):
        self.phase += 0.12
        self.x += self.dx + wind;  self.x %= max(w - 2, 1)
        self.y += self.dy
        if self.y < 2 or self.y > h // 2:
            self.dy *= -1


# ── Colour setup ─────────────────────────────────────────────────────────────

def init_colors():
    # pairs 1-7 in the canonical ROYGBMW order
    fg = [
        curses.COLOR_RED,
        curses.COLOR_YELLOW,
        curses.COLOR_GREEN,
        curses.COLOR_CYAN,
        curses.COLOR_BLUE,
        curses.COLOR_MAGENTA,
        curses.COLOR_WHITE,
    ]
    for i, c in enumerate(fg, start=1):
        curses.init_pair(i, c, -1)


def bpair(n):
    """Bold + color pair – the combination that produces vivid distinct hues."""
    return curses.color_pair(n) | curses.A_BOLD


# ── Scene geometry ────────────────────────────────────────────────────────────

def build_grass(w):
    return "".join(random.choice(["|", "/", "\\"]) for _ in range(max(1, w - 1)))


def build_flowers(w, theme):
    """
    Return list of (col, emoji) pairs evenly spread across the bottom.
    Minimum 4-col gap prevents emoji overlap (each emoji = 2 display cols).
    """
    flowers = THEMES[theme]["flowers"]
    positions = []
    x = 2
    while x < w - 4:
        if random.random() < 0.55:
            positions.append((x, random.choice(flowers)))
        x += random.randint(4, 7)   # ≥4 so adjacent emoji never collide
    return positions


def _stem(wind):
    """Single-char stem that leans with the wind."""
    if   wind >  0.5: return "╱"
    elif wind < -0.5: return "╲"
    else:             return "│"


def draw_scene(stdscr, h, w, static_grass, flowers, wind):
    sc = _stem(wind)

    # row h-5 → flower heads
    for col, emoji in flowers:
        try: stdscr.addstr(h - 5, col, emoji, bpair(random.randint(1, 6)))
        except Exception: pass

    # rows h-4 and h-3 → stems (always centred under the emoji = col)
    for col, _ in flowers:
        for row in (h - 4, h - 3):
            try: stdscr.addstr(row, col, sc, bpair(3))
            except Exception: pass

    # row h-2 → static grass
    try: stdscr.addstr(h - 2, 0, static_grass[: w - 1], bpair(3))
    except Exception: pass


def draw_celestial(stdscr, night, w):
    art = MOON_ART if night else SUN_ART
    col = max(0, w - 9)
    clr = bpair(2)   # yellow for both sun glow and moon glow
    for i, line in enumerate(art):
        try: stdscr.addstr(1 + i, col, line, clr)
        except Exception: pass


# ── Main loop ────────────────────────────────────────────────────────────────

def main(stdscr, count, theme):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.use_default_colors()
    init_colors()

    h, w = stdscr.getmaxyx()

    butterflies = [Butterfly(w, h) for _ in range(count)]
    fireflies   = [Firefly(w, h)   for _ in range(50)]

    wind        = 0.0
    rain        = False
    forced_night = None          # None → auto cycle

    # thunder state
    THUNDER_DUR  = 28            # frames the strike stays visible
    t_frames     = 0
    t_row = t_col = 0            # position of current strike

    # static scene (rebuilt only on resize)
    grass   = build_grass(w)
    flowers = build_flowers(w, theme)
    last_hw = (h, w)
    start   = time.time()

    while True:
        h, w = stdscr.getmaxyx()

        # rebuild static scene on resize
        if (h, w) != last_hw:
            grass   = build_grass(w)
            flowers = build_flowers(w, theme)
            last_hw = (h, w)

        # day / night determination
        elapsed  = time.time() - start
        daylight = (math.sin(elapsed / 25) + 1) / 2
        night    = (daylight < 0.35) if forced_night is None else forced_night

        stdscr.erase()

        # ── header ──────────────────────────────────────────────────────────
        creature_info = f"Fireflies:{len(fireflies)}" if night else f"Butterflies:{len(butterflies)}"
        hdr = (
            f" Theme:{theme}  Wind:{wind:+.1f}  "
            f"{creature_info}  "
            f"{'Night' if night else 'Day '} "
            f"| [d]ay [n]ight [b]+ [↑↓]count [r]ain [t]heme [←→]wind [q]uit"
        )
        try: stdscr.addstr(0, 0, hdr[: w - 1], bpair(7))
        except Exception: pass

        draw_celestial(stdscr, night, w)
        draw_scene(stdscr, h, w, grass, flowers, wind)

        # ── rain & thunder ───────────────────────────────────────────────────
        if rain:
            # raindrops
            for _ in range(max(12, w // 5)):
                try:
                    stdscr.addstr(
                        random.randint(1, h - 6),
                        random.randint(0, w - 2),
                        "|", bpair(5),
                    )
                except Exception: pass

            # trigger a new strike at a completely random screen position
            if t_frames == 0 and random.random() < 0.020:
                t_frames = THUNDER_DUR
                t_row = random.randint(2, max(3, h - 7))
                t_col = random.randint(2, max(3, w - 18))

            # draw active strike
            if t_frames > 0:
                # bright bolt label
                label = "⚡THUNDER⚡"
                try: stdscr.addstr(t_row, t_col, label, bpair(2))
                except Exception: pass

                # scatter extra bolts for the first burst of frames
                if t_frames > THUNDER_DUR - 8:
                    for _ in range(5):
                        br = random.randint(max(1, t_row - 3), min(h - 6, t_row + 3))
                        bc = random.randint(max(0, t_col - 4), min(w - 3, t_col + len(label) + 4))
                        try: stdscr.addstr(br, bc, "⚡", bpair(2))
                        except Exception: pass

                t_frames -= 1

        # ── night: fireflies only ────────────────────────────────────────────
        if night:
            for ff in fireflies:
                ff.update(w, h, wind)
                glow = math.sin(ff.phase)
                if glow > 0:
                    attr = bpair(2) if glow > 0.6 else curses.color_pair(7)
                    try: stdscr.addstr(int(ff.y), int(ff.x), "✦" if glow > 0.6 else "·", attr)
                    except Exception: pass

        # ── day: butterflies only ────────────────────────────────────────────
        else:
            for b in butterflies:
                b.update(wind, w, h)
                try:
                    stdscr.addstr(int(b.y), int(b.x), WING_FRAMES[b.frame], bpair(b.color))
                except Exception: pass

        stdscr.refresh()

        # ── input ────────────────────────────────────────────────────────────
        key = stdscr.getch()
        if   key == ord("q"): break
        elif key == ord("d"): forced_night = False
        elif key == ord("n"): forced_night = True
        elif key == ord("b"): butterflies.append(Butterfly(w, h))
        elif key == ord("r"): rain = not rain
        elif key == ord("t"):
            names  = list(THEMES.keys())
            theme  = names[(names.index(theme) + 1) % len(names)]
            flowers = build_flowers(w, theme)   # rebuild with new theme's emoji
        elif key == curses.KEY_UP:
            if night:
                fireflies.append(Firefly(w, h))
            else:
                butterflies.append(Butterfly(w, h))
        elif key == curses.KEY_DOWN:
            if night and len(fireflies) > 1:
                fireflies.pop()
            elif not night and len(butterflies) > 1:
                butterflies.pop()
        elif key in (curses.KEY_RIGHT, ord("w")):
            wind = round(min(wind + 0.2, 3.0), 1)
        elif key == curses.KEY_LEFT:
            wind = round(max(wind - 0.2, -3.0), 1)

        time.sleep(1 / 30)


def main_cli():
    """Entry point for the `butterfly` command installed by Homebrew / pip."""
    parser = argparse.ArgumentParser(
        description="Animated butterfly garden in your terminal."
    )
    parser.add_argument("--count", type=int, default=20,
                        help="Starting number of butterflies (default: 20)")
    parser.add_argument("--theme", default="spring",
                        choices=list(THEMES.keys()),
                        help="Colour theme (default: spring)")
    args = parser.parse_args()
    curses.wrapper(main, args.count, args.theme)


if __name__ == "__main__":
    main_cli()
