import curses
import time

# screen=curses.initscr()


# curses.noecho()
# curses.cbreak()
# screen.keypad(1)
def main(screen):
    curses.curs_set(0)
    screen.addstr(7,8,"Hello...")
    screen.refresh()
    time.sleep(4)

curses.wrapper(main)
# curses.echo()
# curses.nocbreak()
# screen.keypad(False)

# curses.endwin()