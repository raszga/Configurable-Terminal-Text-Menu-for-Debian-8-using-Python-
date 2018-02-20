# Window(s) Configurable Terminal Text Menu (Debian 8) using Python

*****************************************************
Important note : the example is using pygame joystick for reading a number of Joysticks.

Pygame which has to be re-compiled to avoid the debug printing on the terminal screen screen.

I found the instructions to fix the issue :

How not to have pygame wiritting on console - follow exactly

cd /tmp

sudo apt-get build-dep pygame

apt-get source pygame

nano pygame-1.9.1release+dfsg/src/joystick.c

#search for the printf("SDL.. messages and put a // in front

apt-get source --compile pygame

ls *.deb

#next command put the deb file which you found

sudo dpkg -i python-pygame_1.9.1release+dfsg-9ubuntu1_amd64.deb

#can be different name

url : https://stackoverflow.com/questions/2125702/how-to-suppress-console-output-in-python/25061573

****************************************************************
It happened quite few times that I needed to present data in the text terminal accessible under Debian 8 Linux Dist.

The data broadcast in the terminal has the advantage of being free from the IDLE  and being able to run the Python program as a system command 

Story short after I searched the Internet I decided to try to build my own version which is a "copy" of an old menu program I wrote in Turbo Pascal 7 under MS.DOS

As you would expect even if I like and use Python (2.7)  my  Pascal experience makes the code slightly more conventional...

The basic idea is to creeate a key driven set of menus in Python using the standard terminal configuration ( so a text only screen)

The menus are configurable and described in text files which can be edited and exteneded as needed.

The basic navigation is made by using the arrow keys by using curses

The example uploaded  needs one or more  USB Joystick(s) connected to the computer to run but if you start from IDLE the Start2.py it is tolerant to errors and if you don't have the Joystick the rest of demo will work fine.

To work in the  terminal, open a terminal,
change folder with cd to tthe PYM folder and type idle
loaad and start Start2.py
