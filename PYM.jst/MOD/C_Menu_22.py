#!/usr/bin/env python
import os
import sys
import curses
import curses.wrapper
import traceback
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from C_VAR import *
#===============================================================================
class MenWind(object):
    """
    This object is a typical window menu scalable with the content """
    def __init__(self,HW=1,WW=1,
                 YW=0,XW=0,NW=1,
                 TMsg='Window title',BMsg=' @CR2875-Jan 2018@',
                 Lines=['1-L1--------',
                        '2-L2--------',
                        '3-L3--------',
                        'E-Exit------'],
                 Cols=None,
                 FileName=None):

        curses.initscr()
        #curses.start_color()
        curses.curs_set(1)
        curses.noecho()
        curses.flushinp()
        curses.cbreak()

        self.screen = curses.initscr()
        self.screen.keypad(1)
        self.screen.nodelay(False)
        self.maxY,self.maxX=self.screen.getmaxyx()
        a=[]
        self.N=NW
        self.H=HW
        self.W=WW
        self.X=XW
        self.Y=YW
        self.T=TMsg
        self.B=BMsg
        self.L=[]
        self.C=Cols
        self.FN=FileName
        
        if self.FN!=None:
            fp=open(self.FN)
            self.L=[]
            self.L=fp.read().splitlines()
            fp.close()
            self.T=self.FN
        else:
            self.L=Lines

        for i in range(len(self.L)):
                       a.append(len(self.L[i]))
                       
        self.W=max(len(self.T),len(self.B),max(a))+2
        self.H=2+len(self.L)
        a=[]
        self.drw()
        self.clr()
        
    def cleanup(self):
        curses.doupdate()
        curses.endwin()
        
    def drw(self):
        self.win=curses.newwin(self.H,self.W,self.Y,self.X)
        self.win.box(0,0)
        self.win.addstr(0,1,self.T,curses.A_REVERSE)
        for i in range(len(self.L)):
            self.win.addstr(1+i,1,self.L[i])
        if self.B!='':
            self.win.addstr(i+2,1,self.B,curses.A_BOLD)    
        self.win.refresh()
        curses.doupdate()

    def SendMsg(self):
        self.win.addstr(self.H-1,1,self.B,curses.A_BOLD)    

    def clr(self):
        self.win.clear()
        self.win.refresh()
        curses.doupdate()

    def navigate(self):
        self.drw()
        self.win.move(0,1)
        self.win.refresh()
        i=0
        ckey=0
        self.poz=0
        while (ckey!=27)*(ckey!=10):
            self.poz=0
            ckey=self.screen.getch()
            curses.flushinp()
            if ckey==259:
                i=i-1
            if ckey==258:
                i=i+1
            if i<1:
                i=(len(self.L))
            if i>(len(self.L)):
                i=1
            if ckey==10:
                self.poz=i
            self.drw()
            self.win.addstr(i,1,self.L[i-1],curses.A_REVERSE)
            self.B='sel='+str(100*self.N+i)
            self.SendMsg()
            self.win.refresh()
        if ckey==27:
            self.poz=len(self.L)
        self.sel=100*self.N+self.poz
        self.clr()
        if self.poz==len(self.L):
            self.sel=0
        return self.sel

    def TestKey(self):
        ckey=0
        while ckey!=27:
            ckey=self.screen.getch()
            curses.flushinp()
            print ckey
#===============================================================================
class TopMenu(MenWind):
    def __init__(self,FileName=None):
        MenWind.__init__(self,HW=5,WW=1,
                         YW=1,XW=1,NW=0,
                         TMsg='Top I2C Core Menu',
                         BMsg='@CR2875@',
                         Cols=['C1   ',
                               'C2   ',
                               'C3   ',
                               'C4   ',
                               'Exit  '
                        ])
        self.screen.nodelay(False)
        self.H=5
        self.X=0
        self.Y=0
        self.W=0
        self.FN=FileName
        self.CI=[]
        
        
        if self.FN!=None:
            fp=open(self.FN)
            self.C=[]
            self.C=fp.read().splitlines() 
            fp.close
            self.T=self.FN
            
        for i in range(len(self.C)):
            self.C[i]='|'+self.C[i]+' '
            self.W+=len(self.C[i])
        self.W+=2
        self.CI=[1]
        dx=1
        for j in range(len(self.C)-1):
            dx=dx+len(self.C[j])
            self.CI.append(dx)
        
    def drw(self):
        self.win=curses.newwin(self.H,self.W,self.Y,self.X)
        self.win.box(0,0)
        self.win.addstr(0,1,self.T,curses.A_REVERSE)
        self.win.addstr(2,1,self.C[0])
        for i in range(1,len(self.C)):
                self.win.addstr(2,self.win.getyx()[1],self.C[i])  
        if self.B!='':
            self.win.addstr(4,1,self.B,curses.A_BOLD)
        self.win.refresh()
        curses.doupdate()

    def navigate(self):
        self.drw()
        self.win.move(2,1)
        self.win.refresh()
        i=0
        ckey=0
        i=0
        while (ckey!=27)*(ckey!=10)*(ckey!=258):
            ckey=self.screen.getch()
            curses.flushinp()
            if ckey==260:
                i=i-1
            if ckey==261:
                i=i+1
            if i<0:
                i=(len(self.C)-1)
            if i>(len(self.C)-1):
                i=0
            if (ckey==10):
                self.poz=i
            elif (ckey==258):
                self.poz=i                
            self.drw()
            self.B='Sel='+str(i+1)
            self.SendMsg()
            self.win.addstr(2,self.CI[i],self.C[i],curses.A_REVERSE)
            self.win.refresh()
        if ckey==27:
            self.poz=len(self.C)-1
        self.sel=100*self.N+self.poz
        if self.poz==len(self.C)-1:
            curses.endwin()
            exit()
        self.clr()
        return self.sel

    def Gen(self):
        T.drw()
        for i in range(len(T.C)):
            w.append(MenWind(XW=T.CI[i],
                             YW=3,
                             NW=i+1,
                             TMsg=T.C[i],
                             FileName=FLDs+T.C[i][1:(len(T.C[i])-1)]+'.txt'
                             )
                     )

    def SelfGen(self,NL=5):
        for i in range(len(T.C)):
            #print T.C[i]
            fp=open(FLDs+T.C[i][1:(len(T.C[i])-1)]+'.txt','w')
            fp.close()
            
        for i in range(len(T.C)):
            fp=open(FLDs+T.C[i][1:(len(T.C[i])-1)]+'.txt','a')
            for j in range(NL):
                fp.write(str(j+1)+' - '+'Line'+str(j+1)+'\n')
            fp.write('E - Exit')
        fp.close
#===============================================================================
class WorkingWindow(MenWind):
    def __init__(self,HW=25,WW=40,TMsg='',Lines=['']):
        MenWind.__init__(self,HW=1,WW=1,
                         YW=1,XW=1,NW=0,
                         TMsg='Working Window',
                         BMsg='@CR2875@',
                         Lines=['']
                         )
        self.screen.nodelay(False)
        self.HW=self.maxY
        self.WW=self.maxX
        Lines=[]
        # Creeate the empty lines...
        for i in range(self.HW-2):
            Lines.append(' '*(self.WW-2))
            
        PLN=Lines
        MenWind.__init__(self,HW=1,WW=1,
                         YW=0,XW=0,NW=0,
                         TMsg='Working Window',
                         BMsg='@CR2875@',
                        Lines=PLN)
#===============================================================================
class RCT(object):
    def __init__(self,XR=0,YR=0,HR=3,WR=3,SMB=''):
        self.X=XR
        self.Y=YR
        self.H=HR
        self.W=WR
        self.S=SMB
        curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.flushinp()
        curses.cbreak()
        self.screen = curses.initscr()
        self.screen.keypad(1)
        self.screen.nodelay(False)
        self.maxY,self.maxX=self.screen.getmaxyx()
        self.win=curses.newwin(self.H,self.W,self.Y,self.X)
        

    def drw(self):
        self.win=curses.newwin(self.H,self.W,self.Y,self.X)
        self.win.box(0,0)
        self.win.refresh()

    def clr(self):
        self.win.clear()
        #self.win.refresh()

    def bar(self,Vin):
        self.Nmax=self.win.getmaxyx()[1]-4
        self.sl,self.sl0=bar ( Nmax=self.Nmax,Vmax=5.0,V=Vin,SMB='=')
        self.win.addstr(1,1,self.sl0)
        self.win.addstr(1,1,self.sl)
        self.win.refresh()
#===============================================================================
class bar_meter(object):
    def __init__(self,XM=1,YM=1,WM=80,HM=3,Vmax=5,V=0,NT='AN '):
        curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.flushinp()
        curses.cbreak()
        self.stdscr = curses.initscr()
        self.stdscr.keypad(1)
        self.stdscr.nodelay(False)
        self.X=XM
        self.Y=YM
        self.H=HM
        self.W=WM
        self.V=V
        self.Vmax=Vmax
        self.NT=NT
        self.sl=''
        self.sl0=''
        self.win=curses.newwin(self.H,self.W,self.Y,self.X)
        self.Ymax,self.Xmax=self.win.getmaxyx()
        
    def drw(self):
        self.win=curses.newwin(self.H,self.W,self.Y,self.X)
        self.win.box(0,0)
        self.win.refresh()
        
    def bar( self,SMB='|'):
        Lmax=self.W
        Lamp=Lmax-2-len(self.NT)-6
        Ampl=Lamp
        Ampl=int((Ampl*self.V)/self.Vmax)-2
        self.sl=self.NT+format(self.V,'6.2f')+Ampl*SMB+'<'
        self.sl0=(Lmax-2)*'+'
        return self.sl,self.sl0

    def drw_Meter(self):
        curses.curs_set(0)
        self.drw()
        self.bar()
        self.win.addstr(1,1,self.sl0)
        self.win.addstr(1,1,self.sl,curses.A_REVERSE)
        self.win.refresh()
        curses.curs_set(0)

    def drw_DIO(self):
        curses.curs_set(0)
        self.drw()
        self.sl0=(self.win.getmaxyx()[1]-2)*' '
        self.win.addstr(1,1,self.sl0)
        self.win.addstr(1,1,self.NT)
        self.sl=(self.V!=0)*(len(self.sl0)-len(self.NT)-1)*' '
        self.win.addstr(1,len(self.NT)+1,self.sl,curses.A_REVERSE)
        self.win.refresh()
        curses.curs_set(0)
#===============================================================================
class inp_win(RCT):
    def __init__(self,XR=0,YR=0,
                 HR=3,WR=3,
                 SMB='Value=',
                 Vmin=-1000.00,Vmax=-1000.00,DF=0):
        
        self.X=XR
        self.Y=YR
        self.H=HR
        self.W=WR
        self.S=SMB
        self.Vmax=Vmax
        self.Vmin=Vmin
        self.DF=DF
        if (self.DF<self.Vmin)|(self.DF>self.Vmax):
            self.DF=float((self.Vmax+self.Vmin)/2.0)
        curses.curs_set(0)
        curses.echo()
        curses.flushinp()
        curses.cbreak()
    
    def get_val(self):
        curses.echo()
        self.W=8+len(self.S)+3*max(len(str(self.Vmin)),
                                 len(str(self.Vmax)))
        
        self.maxY,self.maxX=self.H,self.W
        self.ret=2*self.Vmin
        self.drw()
        y,x=self.win.getyx()
        try:
            while (self.ret < self.Vmin)|(self.ret>self.Vmax):
                self.win.addstr(1,1,self.S)
                y,x=self.win.getyx()
                self.win.addstr(y,x,str(self.Vmin)+'|',curses.A_REVERSE)
                y,x=self.win.getyx()
                self.win.addstr(y,self.maxX-2-len(str(self.Vmax)),'|'+str(self.Vmax),curses.A_REVERSE)
                
                self.ret=float(self.win.getstr(y,x+1,
                                         max( len(str(self.Vmin)),len(str(self.Vmax)))
                                         ))
        except:
            self.ret=float(self.DF)
            pass
        self.win.addstr(y,x+1,str(self.ret),curses.A_REVERSE)
        curses.noecho()
        curses.beep()
        self.win.refresh()
        return self.ret      
#===============================================================================
def bar ( Nmax=40,Vmax=5.0,V=0,SMB='='):
    Ampl=Nmax
    Ampl=int((Ampl*V)/Vmax)-1
    sl=format(V,'6.4f')+Ampl*SMB+'>'
    sl0=(Nmax+len(format(50,'6.4f')))*' '
    return sl,sl0
#-------------------------------------------------------------------------------
def bar_drw(W,y,x,Vin):
    W.win.addstr(y,x,bar(V=Vin)[1])
    W.win.addstr(y,x,bar(V=Vin)[0])
    return



# ------------------Test -------------------------------------
execfile(MODs+'C_ini.py')
