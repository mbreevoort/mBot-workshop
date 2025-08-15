from lib.mBot import *
import unicurses as uc

def main():
    # Initialize screen (returns a WINDOW pointer, not a Python object)
    stdscr = uc.initscr()
    uc.cbreak()
    uc.noecho()
    uc.keypad(stdscr, True)  # Pass the WINDOW pointer explicitly
    bot = findMBot()

    try:
        uc.wmove(stdscr, 0, 0)
        uc.waddstr(stdscr, "Press keys (ESC to exit):")
        uc.wrefresh(stdscr)

        while True:
            ch = uc.wgetch(stdscr)
            if ch == 27:  # ESC key to exit
                break

            if ch == 258:  # DOWN key
                bot.doMove(-100, -100)

            if ch == 259:  # UP key
                bot.doMove(200, 200)

            if ch == 260:  # LEFT key
                bot.doMove(-100, 100)

            if ch == 261:  # RIGHT key
                bot.doMove(100, -100)

            if ch == 32:   # SPACE key
                bot.doMove(0, 0)

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
        bot.doMove(0, 0) # stop the motor
        print ('Bye!')


if __name__ == "__main__":
    main()

