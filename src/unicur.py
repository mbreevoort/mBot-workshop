import unicurses as uc

def main():
    # Initialize screen (returns a WINDOW pointer, not a Python object)
    stdscr = uc.initscr()
    uc.cbreak()
    uc.noecho()
    uc.keypad(stdscr, True)  # Pass the WINDOW pointer explicitly

    try:
        uc.wmove(stdscr, 0, 0)
        uc.waddstr(stdscr, "Press keys (ESC to exit):")
        uc.wrefresh(stdscr)

        while True:
            ch = uc.wgetch(stdscr)
            if ch == 27:  # ESC key to exit
                break

            uc.wclear(stdscr)
            uc.wmove(stdscr, 0, 0)
            uc.waddstr(stdscr, "Press keys (ESC to exit):")

            # Display key code and char if printable
            try:
                char_repr = chr(ch) if 32 <= ch <= 126 else 'non-printable'
            except ValueError:
                char_repr = 'non-printable'

            uc.wmove(stdscr, 1, 0)
            uc.waddstr(stdscr, f"Key pressed: {ch} ({char_repr})")
            uc.wrefresh(stdscr)

    finally:
        uc.keypad(stdscr, False)
        uc.echo()
        uc.nocbreak()
        uc.endwin()
        print ('Bye!')


if __name__ == "__main__":
    main()
