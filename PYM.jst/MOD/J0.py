#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame as pyg
import sys
import os

pyg.init()
pyg.joystick.init()
JNmax=pyg.joystick.get_count()
def All_Joy_init():
    J=[]
    for i in range(JNmax):
        J.append(JY(JN=i))
    return J

class JY(object):
    def __init__(self,JN=0):
        self.J=pyg.joystick.Joystick(JN)
        self.J.init()
        self.NAX=self.J.get_numaxes()
        self.NBT=self.J.get_numbuttons()
        self.NAM=self.J.get_name()
        self.NBALL=self.J.get_numballs()
        self.NHAT=self.J.get_numhats()
        self.JN=self.J.get_id()
        self.JNmax=JNmax

    def read_axis(self):
        self.Jax=[]
        pyg.event.pump()
        for i in range(self.NAX):
            self.Jax.append(self.J.get_axis( i ))
        return  self.Jax

    def read_bt(self):
        self.Jbt=[]
        pyg.event.pump()
        for i in range(self.NBT):
            self.Jbt.append(self.J.get_button( i ))
        return self.Jbt
    
    def read_hat(self):
        self.Jhat=[]
        pyg.event.pump()
        for i in range(self.NHAT):
            self.Jhat.append(self.J.get_hat(i))
        return self.Jhat
    

##JJ=JY()
##while True:
##    AX,BT= JJ.Joy_Read()
##    print AX
"""
pygame.joystick.init	—	Initialize the joystick module.
pygame.joystick.quit	—	Uninitialize the joystick module.
pygame.joystick.get_init	—	Returns True if the joystick module is initialized.
pygame.joystick.get_count	—	Returns the number of joysticks.
pygame.joystick.Joystick	—	Create a new Joystick object.
pygame.joystick.Joystick.init	—	initialize the Joystick
pygame.joystick.Joystick.quit	—	uninitialize the Joystick
pygame.joystick.Joystick.get_init	—	check if the Joystick is initialized
pygame.joystick.Joystick.get_id	—	get the Joystick ID
pygame.joystick.Joystick.get_name	—	get the Joystick system name
pygame.joystick.Joystick.get_numaxes	—	get the number of axes on a Joystick
pygame.joystick.Joystick.get_axis	—	get the current position of an axis
pygame.joystick.Joystick.get_numballs	—	get the number of trackballs on a Joystick
pygame.joystick.Joystick.get_ball	—	get the relative position of a trackball
pygame.joystick.Joystick.get_numbuttons	—	get the number of buttons on a Joystick
pygame.joystick.Joystick.get_button	—	get the current button state
pygame.joystick.Joystick.get_numhats	—	get the number of hat controls on a Joystick
pygame.joystick.Joystick.get_hat	—	get the position of a joystick hat

How not to have pygame wiritting on console - follow exactly

cd /tmp
sudo apt-get build-dep pygame
apt-get source pygame
nano pygame-1.9.1release+dfsg/src/joystick.c
# search for the printf("SDL.. messages and put a // in front
apt-get source --compile pygame
ls *.deb
# next command put the deb file which you found
sudo dpkg -i python-pygame_1.9.1release+dfsg-9ubuntu1_amd64.deb
# can be different name

"""
