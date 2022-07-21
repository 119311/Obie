#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter


root = tkinter.Tk()
root.title("Software Title")
root.geometry("400x300")

# ラベル
Static1 = tkinter.Label(text="test")
Static1.pack()

root.mainloop()

"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Radiobutton 1')

# Frame
frame1 = ttk.Frame(root, padding=10)
# Style - Theme
ttk.Style().theme_use('classic')
# Label Frame
label_frame = ttk.Labelframe(
    frame1,
    text='Options',
    padding=(10),
    style='My.TLabelframe')

# Radiobutton 1
v1 = StringVar()
rb1 = ttk.Radiobutton(
    label_frame,
    text='Option A',
    value='A',
    variable=v1)

# Radiobutton 2
rb2 = ttk.Radiobutton(
    label_frame,
    text='Option B',
    value='B',
    variable=v1)

# Button
button1 = ttk.Button(
    frame1,
    text='OK',
    padding=(20, 5),
    command=lambda : print("v1=%s" % v1.get()))

# Layout
frame1.grid()
label_frame.grid(row=0, column=0)
rb1.grid(row=0, column=0) # LabelFrame
rb2.grid(row=0, column=1) # LabelFrame
button1.grid(row=1, pady=5)

# Start App
root.mainloop()

"""
