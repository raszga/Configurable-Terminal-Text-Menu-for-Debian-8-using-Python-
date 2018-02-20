WW.clr()
WW.drw()
curses.echo()
curses.noecho()
curses.flushinp()
curses.curs_set(0)
WW.B=''
WW.SendMsg()
rr=RCT()
rr.H=2
rr.W=2
    

for i in range(int(WW.win.getmaxyx()[1]/2)):
    rr.X=2*i
    for j in range(int(WW.win.getmaxyx()[0]/2)):
        rr.Y=2*j
        rr.drw()
        rr.win.refresh()
WW.win.refresh()

while AstRetC()!=115:
    pass

curses.curs_set(1)

