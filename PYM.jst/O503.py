WW.clr()
WW.drw()
WW.B=''
WW.SendMsg()
curses.echo()
curses.curs_set(1)
curses.noecho()
curses.flushinp()
WW.B='Press s to exit'
WW.SendMsg()
WW.win.addstr(3,1,' Program Path parameters ',curses.A_REVERSE)
WW.win.addstr(4,1,'Main Program Path:  '+ PTH)
WW.win.addstr(5,1,'Program Modues:     '+ MODs)
WW.win.addstr(6,1,'Program Menu Files: '+FLDs)
WW.win.addstr(7,1,'Total  of JSTK      : '+str(JNmax))
WW.win.refresh()
iw=inp_win(1,8,
           SMB='Test Value input=',
           Vmin=-9999.00,Vmax=9999.00,DF=1000)
ss=iw.get_val()
iw=inp_win(1,11,
           SMB='Test1 Value1 input=',
           Vmin=-89.00,Vmax=89.00,DF=50)
ss=iw.get_val()
while AstRetC()!=115:
    pass
curses.curs_set(1)
