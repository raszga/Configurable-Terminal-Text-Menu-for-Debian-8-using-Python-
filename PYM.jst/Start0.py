import sys
import os
sys.path.append(os.getcwd()+'/MOD') # define local folder for loading modules
from C_VAR import * # The general variable module, load it in every other
from C_Menu_22 import *
from KY_1 import *

T.Gen()
while True:
    T.navigate()
    T.drw()
    w[T.sel].navigate()
    WW.T=w[T.sel].T+' '+str(w[T.sel].sel)
    WW.drw()
    WW.B='Sel:'+str(w[T.sel].sel)
    strg=str(int(w[T.sel].sel))
    strg='O'+strg+'.py'
    WW.B+= '>>s-to-go-back,  .py File: is '+strg
    WW.SendMsg()
#-----------------------------------------------------
    execfile(strg)
#------------------------------------------------------
    strg=''
    WW.B=''
    WW.win.refresh()
    curses.flushinp()
    WW.screen.getch()
    WW.clr()
curses.endwin()
