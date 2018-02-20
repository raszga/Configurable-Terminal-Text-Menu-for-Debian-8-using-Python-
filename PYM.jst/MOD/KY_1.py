#!/usr/bin/env python
import curses
stdscr = curses.initscr()

def AstC(C='c',M='To Continue',Mdysp=True,Ret=False):
    """
    this function waits for a char to be pressed in itself
    it will stay inside of the loop as long the char is not  prressed
    C - The character to be pressed
    M - initial message ( printed if Mdysp=True)
    Ret - returning message is printed if True
    """
    msg=[]

    stdscr.nodelay(1)

    if Mdysp:
        msg= 'Press '+ C+' ' +M    

    while stdscr.getch==-1:
        curses.flushinp()
        pass
    
    curses.halfdelay(1)

    while  stdscr.getch()!=ord(C):
        curses.flushinp()
        pass
    
    if Ret:
        msg='Pressed '+ C
    stdscr.nodelay(0)
    curses.flushinp()

    return msg

def Ast0(C='c',M='To Continue',Mdysp=False):
    """   
    this function waits for a char to be pressed in but exits with False if not
    it will stay inside of the loop as long the char is not  prressed
    C - The character to be pressed
    M - initial message ( printed if Mdysp=True)
    RT - the return message 
    """
    curses.flushinp()
    curses.flushinp()
    curses.flushinp()
    curses.flushinp()
    RT=False
    msg=[]
    if Mdysp:
        msg= 'Press '+ C+' ' +M    
    stdscr.nodelay(1)
    if stdscr.getch==-1:
        curses.flushinp()
        pass
    else:
        curses.halfdelay(1)
        if stdscr.getch()==ord(C):
            curses.flushinp()
            RT=True
    stdscr.nodelay(0)
    curses.flushinp()
    return RT,msg

def AstRetC():
    """
    this function waits for a char to be pressed
    and returns the character if pressed
    it will exit  of the loop as long the char is not  prressed
    C - The character pressed ord code
    """
    C=-1
    stdscr.nodelay(1)
    if stdscr.getch==-1:
        curses.flushinp()
        pass
    else:
        curses.halfdelay(1)
        C=stdscr.getch()
        curses.flushinp()
    stdscr.nodelay(0)
    curses.flushinp()
    return C

def Ast0RetC():
    """
    this function waits for a char to be pressed
    and returns the character if pressed
    it will exit  of the loop as long the char is not  prressed
    C - The character pressed ord code
    """
    C=-1
    stdscr.nodelay(1)
    while stdscr.getch==-1:
        curses.flushinp()
        pass
    curses.halfdelay(1)
    C=stdscr.getch()
    curses.flushinp()
    stdscr.nodelay(0)
    curses.flushinp()
    return C

def TestKey():
    stdscr.nodelay(False)   
    return stdscr.getch()


