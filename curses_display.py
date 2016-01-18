#!/usr/bin/env python

import curses

myscreen = curses.initscr()

# curs_set(0)

myscreen.border(0)

myscreen.addstr(1, 2, "-----6--4--2-")
myscreen.addstr(2, 2, "--2-----4--2-")
myscreen.addstr(3, 2, "-----0-------")
myscreen.addstr(4, 2, "0----2-------")
myscreen.addstr(5, 2, "0-------3--0-")
myscreen.addstr(6, 2, "0-------2--0-")

myscreen.addstr(7, 2, "     ^       ")

myscreen.refresh()

myscreen.getch()

myscreen.addstr(7, 2, "         ^   ")
# int y, x;            // to store where you are
# getyx(stdscr, y, x); // save current pos
# myscreen.move(7, 2);
# myscreen.clrtoeol()

myscreen.getch()

myscreen.addstr(7, 2, "           ^ ")
# move(y, x);          // move back to where you were


myscreen.getch()

curses.endwin()
