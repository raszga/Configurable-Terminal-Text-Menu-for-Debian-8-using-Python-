WW.B+= ' ** Press s to go back '
WW.SendMsg()
i=220
while AstRetC()!=115:
    WW.win.addstr(2,2,str(i))
    i+=1
    WW.win.refresh()
    
