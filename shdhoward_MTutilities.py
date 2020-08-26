### shd python utilities -- tkinter and file

import os
import numpy as np
import scipy

get_ipython().magic('matplotlib inline')
import tkinter
from tkinter import Tk
from tkinter import *
from tkinter import ttk

##from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd


def SelectFile (format):
    # open geosoft grid
    Tk().withdraw() # keep the root window from appearing

    # show an "Open" dialog box and return the path to the selected file
    if (format == 'grd'):
        filename = fd.askopenfilename(title = "Select geosoft grd file ",filetypes = (("geosoft grid files","*.grd"),("all files","*.*")))
    elif (format == 'gdb'):
        filename = fd.askopenfilename(title = "Select gdb file",filetypes = (("database files","*.gdb"),("all files","*.*")))
    elif (format == 'aseg'):
        filename = fd.askopenfilename(title = "Select aseg-gdf2 dfn file",filetypes = (("aseg-gdf2 dfn","*.dfn"),("all files","*.*")))
    elif (format == 'seismic'):
        filename = fd.askopenfilename(title = "Select seismic file",filetypes = (("sac files","*.sac"),("mseed files","*.mseed"), ("all files","*.*")))
    elif (format == 'raster'):
        filename = fd.askopenfilename(title = "Select raster  file",filetypes = (("tif files","*.tif"),("jp2 files","*.jp2"), ("all files","*.*")))
    elif (format == 'edi'):
        filename = fd.askopenfilename(title = "Select edib file",filetypes = (("database files","*.edi"),("all files","*.*")))        
    else:
        # msg = Message(master, text = format + "format is not supported!")
        return ''

    if filename =="":
        master = Tk()
        Button(master, text="Quit", command=root.destroy).pack()
        msg = Message(master, text = "No file selected!")
        msg.pack()
        master.mainloop()
    return filename

def SelectDir():
    Tk().withdraw() # keep the root window from appearing
    dir = fd.askdirectory()
    return dir


def GetFileInfo(filename):
    dirname = os.path.dirname(filename)
    file = os.path.basename(filename)
    fileNoExt = os.path.splitext(file)[0]
    return dirname, file, fileNoExt




