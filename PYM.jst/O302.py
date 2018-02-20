WW.clr()
WW.drw()
curses.echo()
curses.noecho()
curses.flushinp()
curses.curs_set(0)
WW.B='Press s   to exit up'
WW.SendMsg()
while AstRetC()!=115:
    for i in range(12):
        VR=r=AN[i].Read_Stat(5,PL='')[2]
        WW.win.addstr(i+2,2,'AN'+format(i,'2.0f')+':')
        bar_drw(WW,WW.win.getyx()[0],WW.win.getyx()[1],VR)
    WW.win.refresh()
curses.curs_set(1)

