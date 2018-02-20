WW.clr()
WW.drw()
WW.B=''
WW.SendMsg()
curses.echo()
curses.curs_set(1)
curses.noecho()
curses.flushinp()
WW.B='s=to-go-back'
WW.SendMsg()
curses.curs_set(0)
Brm=bar_meter()
Brm.W=25
t0=time()
JJ=All_Joy_init()

while AstRetC()!=115:
    for i in range (JNmax):
        J=JJ[i]
        WW.win.addstr(1,1+45*i,'Joystick Parameters screen',curses.A_REVERSE)
        WW.win.addstr(2,1+45*i,'Joystick Count : '+format(J.JNmax,'2.0f'))
        WW.win.addstr(3,1+45*i,'Joystick Current : '+format(J.JN,'2.0f'))
        WW.win.addstr(4,1+45*i,'Joystick N Axes : '+format(J.NAX,'2.0f'))
        WW.win.addstr(5,1+45*i,'Joystick N Buttons : '+format(J.NBT,'2.0f'))
        WW.win.addstr(6,1+45*i,'Joystick N Hats : '+format(J.NHAT,'2.0f'))
        WW.win.addstr(7,1+45*i,'Joystick N Balls : '+format(J.NBALL,'2.0f'))
        WW.win.addstr(8,1+45*i,'Joystick Name :'+ J.NAM)

        for s in range(J.NAX):
            Brm.W=35
            Brm.NT='Axis:'+format(s,'2.0f')+'='
            Brm.Vmax=2000
            Brm.X=i*45
            Brm.Y=9+3*s
            r=J.read_axis()[s]
            Brm.V=int((1+r)*1000) ## no neg values yet
            Brm.drw_Meter()
            Brm.win.refresh()

        J=JJ[i]

        for s in range(J.NBT):
            Brm.W=10
            Brm.NT='BT:'+format(s,'2.0f')+'='
            Brm.Vmax=2000
            Brm.X=i*45+35
            Brm.Y=9+2*s
            r=J.read_bt()[s]
            Brm.V=r
            Brm.drw_DIO()
            Brm.win.refresh()
         
    WW.win.refresh()
curses.curs_set(1)
