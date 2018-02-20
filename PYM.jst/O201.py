WW.clr()
WW.drw()
WW.B=''
WW.B=' Random bar Test, Press s exit'
WW.SendMsg()
curses.echo()
curses.noecho()
curses.flushinp()
curses.curs_set(0)
WW.SendMsg()
while AstRetC()!=115:
    for i in range(24):
        VR=random.random()*5.00
        bar_drw(WW,i+2,2,VR)
    WW.win.refresh()
curses.curs_set(1)
