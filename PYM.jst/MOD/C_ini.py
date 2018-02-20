#from Core15 import *
import sys
import os
import pygame as pyg
pyg.init()
from J0 import *
from time import *
import random
import string
from C_VAR import *
#print FLDs, MODs
#-----------init windows-----------
w=[]
WW=WorkingWindow()
#-----------Decide Bar menu fields---
T=TopMenu(FileName=FLDs+'JoyTestMenu.txt')
try:
    # id the menu files exist alreay
    T.Gen()
except:
    # otherwise autogenerate the menu with 5 lines
    T.SelfGen()
