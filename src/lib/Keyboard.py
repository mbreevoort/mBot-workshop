import unicurses as uc

# Mapping of keycodes (mac, win, letters) to friendly names
KEY_MAP = {
    258: "DOWN", 456: "DOWN", ord("s"): "DOWN",
    259: "UP",   450: "UP",   ord("w"): "UP",
    260: "LEFT", 452: "LEFT", ord("a"): "LEFT",
    261: "RIGHT",454: "RIGHT",ord("d"): "RIGHT",
    27: "ESC",  # ESC key
    32: "SPACE", # spacebar
}

class Keyboard:
    def __init__(self):
        self.stdscr = uc.initscr()
        uc.noecho()
        uc.cbreak()
        uc.keypad(self.stdscr, True)
        uc.timeout(0)  # non-blocking input
        uc.wmove(self.stdscr, 0, 0)
        uc.waddstr(self.stdscr, "Press keys (ESC to exit):")
        uc.wrefresh(self.stdscr)

    def get_key(self):
        ch = uc.wgetch(self.stdscr)
        if ch == -1:
            return None  # no key pressed

        # Look up special keys
        if ch in KEY_MAP:
            return KEY_MAP[ch]

        # If it's a printable character, return uppercase string
        if 32 <= ch <= 126:   # ASCII printable range
            return chr(ch).upper()

        return None  # unrecognized key


def close(self):
        """Restore terminal settings."""
        uc.nocbreak()
        uc.echo()
        uc.endwin()
