#! /anaconda3/bin/python3 
from tkinter import *
from time import sleep

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

while True:
    s = input("Prompt: ")
    var.set(s)
    root.update_idletasks()
    root.update()
