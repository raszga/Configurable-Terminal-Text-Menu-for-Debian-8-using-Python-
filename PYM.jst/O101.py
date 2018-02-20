WW.clr()
WW.drw()
WW.B=''
WW.SendMsg()
curses.echo()
curses.curs_set(1)
curses.noecho()
curses.flushinp()
WW.B='Press s   to exit up'
WW.SendMsg()
curses.curs_set(0)
Brm=bar_meter()
Brm.W=25
t0=time()
JJ=All_Joy_init()

while AstRetC()!=115:
    for i in range (JNmax):
        J=JJ[i]
        WW.win.addstr(2,1+25*i,' '+J.NAM+' ',curses.A_REVERSE)
        WW.win.addstr(3,1+25*i,'Joy Count  : '+format(J.JNmax,'2.0f'))
        WW.win.addstr(4,1+25*i,'Joy Number : '+format(J.JN,'2.0f'),curses.A_REVERSE)
        WW.win.addstr(5,1+25*i,'Joy N Axes : '+format(J.NAX,'2.0f'))
        WW.win.addstr(6,1+25*i,'Joy N Butt : '+format(J.NBT,'2.0f'))
        WW.win.addstr(7,1+25*i,'Joy N Hats : '+format(J.NHAT,'2.0f'))
        WW.win.addstr(8,1+25*i,'Joy N Balls: '+format(J.NBALL,'2.0f'))
         
    WW.win.refresh()
curses.curs_set(1)
