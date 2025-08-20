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
        uc.timeout(0)

        last_beep = 0
        reverse = False

        while True:
            ch = uc.wgetch(stdscr)
            if ch == 27:  # ESC key to exit
                break

            if ch == 258:  # DOWN key
                bot.doMove(-100, -100)
                reverse = True

            if ch == 259:  # UP key
                reverse = False
                bot.doMove(200, 200)

            if ch == 260:  # LEFT key
                reverse = False
                bot.doMove(-100, 100)

            if ch == 261:  # RIGHT key
                reverse = False
                bot.doMove(100, -100)

            if ch == 32:   # SPACE key
                reverse = False
                bot.doMove(0, 0)

            if (reverse):
                now = time.time()
                if now - last_beep > 1.2:  # every 1.2 seconds
                    bot.doBuzzer(1200, 300)  # 300 milliseconds beep
                    last_beep = now

            uc.wclear(stdscr)
            uc.wmove(stdscr, 0, 0)
            uc.waddstr(stdscr, "Press keys (ESC to exit):")

            # Display key code and char if printable
            try:
                char_repr = chr(ch) if 32 <= ch <= 126 else 'non-printable'
            except ValueError:
                char_repr = 'non-printable'

            uc.wmove(stdscr, 1, 0)
            uc.waddstr(stdscr, f"Key pressed: {ch} ({char_repr})")  # -1 means "no key pressed"
            uc.wrefresh(stdscr)

            sleep(0.1)

    finally:
        uc.keypad(stdscr, False)
        uc.echo()
        uc.nocbreak()
        uc.endwin()
        bot.doMove(0, 0) # stop the motor
        print ('Bye!')


if __name__ == "__main__":
    main()

