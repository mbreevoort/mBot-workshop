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

            if ch == 258 or ch == 456 or ch == 115:  # DOWN key mac, win, s
                bot.doMove(-100, -100)
                reverse = True

            if ch == 259 or ch == 450 or ch == 119:  # UP key mac, win, w
                bot.doMove(200, 200)
                reverse = False

            if ch == 260 or ch == 452 or ch == 97:  # LEFT key mac, win, a
                bot.doMove(-100, 100)
                reverse = False

            if ch == 261 or ch == 454 or ch == 100:  # RIGHT key mac, win, d
                bot.doMove(100, -100)
                reverse = False

            if ch == 32:   # SPACE key
                bot.doMove(0, 0)
                reverse = False

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

