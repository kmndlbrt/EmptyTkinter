# PlaNS

# Version: 2020-04-27 20:00
# Running in Python 3.8.1
# http://github.com/kurtmnd
# Developed by N.S.

'''

TODO list:
- 

Bugs:
- 

'''

############################# STATIC VARIABLES

PROGRAM_NAME_LONG = "Long Name"
PROGRAM_NAME_SHORT = "Empty Prog."

############################# IMPORT PYTHON LIBRARIES

from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import datetime

############################# IMPORT EXTERNAL LIBRARIES

# For Windows open C:\Windows\System32\cmd.exe as administrator



############################# SIMPLE BASIC METHODS

def log(s): print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S | ")+s)
def logError(e,s):
    log("")
    try: log("*** "+s+"\n\n"+str(e)+"\n")
    except:
        log("*** "+s+"\n\n")
        traceback.print_exc()

def from_cwd(file_name): return os.path.join(os.path.dirname(__file__),file_name) # join current directory and file

############################# MAIN METHODS

def set_main_folder(path):
    global a
    try:
        ''
    except Exception as e:
        logError(e,"Some description about this method...")
    
############################# CALLBACKS (GUI METHODS/EVENTS)
    
def b1_event(): # real suffle
    ''
    
def link_event1(event): # link to web of about/author
    webbrowser.open_new(r"https://github.com/kurtmnd")

def on_closing(): # close
    if messagebox.askokcancel(PROGRAM_NAME_SHORT, "Do you want to quit?"):
        try:
            #messagebox.showinfo(PROGRAM_NAME_SHORT, "debug")
            ''
        except Exception as e: logError(e,"")
        root.destroy()

def key_event1(event):
    log("space")
    
############################# GRAPHICAL USER INTERFACE

root = Tk()
#root.wm_attributes("-topmost", 1) # always on top
root.wm_title(PROGRAM_NAME_SHORT)
root.resizable(width=False, height=False)
root.bind("<Key-space>", key_event1)
root.protocol("WM_DELETE_WINDOW", on_closing)

############# TOP BUTTONS

b1 = Button(root, text="Insert a new activity", command=b1_event)
b1.config( height = 1, width = 40, bg="grey", fg="white");
b1.pack()

############# CENTER

headerFrame1 = Frame(root)
headerFrame1.pack()

l7 = Label(headerFrame1, text="")
l7.pack(side=LEFT)

l3 = Label(headerFrame1, text="Add here some widgets...")
l3.config( height = 4);
l3.pack(side=TOP)

############# FOOTER

footerFrame = Frame(root)
footerFrame.pack()

l5 = Label(footerFrame, text="")
l5.pack(side=LEFT)

Label(footerFrame, text="Developed by:").pack(side=LEFT)

l4 = Label(footerFrame, text="github.com/kurtmnd", fg="blue", cursor="hand2")
l4.bind("<Button-1>", link_event1)
l4.pack(side=LEFT)

l6 = Label(footerFrame, text="")
l6.pack(side=LEFT)

############################# INITIALIZATION OF VARIABLES

list_songs = []

############################# INITIAL ROUTINE

try:
    
    log(PROGRAM_NAME_LONG)

except Exception as e:
    logError(e,"Some problems in the initial routine")

mainloop() # start the GUI
