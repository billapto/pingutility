#Import
#use pyinstaller to convert this to a .exe file eg. pyinstaller -w -F ping2.py
#-w removes the console
#-f Exports one file
import os
from tkinter import *


#define window
Window = Tk()
Window.title("Network Utilities")

#define canvas        
canvas1 = Canvas(Window, width = 300, height = 350, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

#add labels
label1 = Label(Window, text='Ping Servers', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 15))
canvas1.create_window(75, 60, window=label1)

label2 = Label(Window, text= os.getlogin(), bg = 'lightsteelblue2')
label2.config(font=('helvetica', 9))
canvas1.create_window(50, 20, window=label2)

#add classes
def PingRouter ():
    os.system('start cmd /k ping.exe 192.168.1.1 -t')
    
button1 = Button(text='      Ping Router    ', command=PingRouter,  bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(85, 90, window=button1)

def PingPrinter ():
    os.system('start cmd /k ping.exe 192.168.1.10 -t') 
    
button2 = Button(text='      Ping Printer    ', command=PingPrinter,  bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(84, 130, window=button2)


def PingDNS ():
    os.system('start cmd /k ping.exe 192.168.1.20 -t' ) 
    
button3 = Button(text='      Ping Internal DNS    ', command=PingDNS,  bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(107, 170, window=button3)

def Quit():
    exit()
    
button10 = Button(text='      Quit    ', command=Quit,  bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(55, 300, window=button10)

Window.mainloop()
