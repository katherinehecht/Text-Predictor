#!/usr/bin/env python3



import sys
import getch
import os
import operator
import requests
import string
import re
import timeit
from tkinter import *

def close_window():
    root.destroy()

def get_key(event):
    global word
    global sentence
    if event.char == 'Return':
        sentence = ''
        word = ''
        real_text['text'] = ' '
    elif ord(event.char) == 127:
        real_text['text'] = real_text['text'][:-1]

    else:
        print(ord(event.char))
        if (event.char).isdigit() :
            word = suggestions[int(event.char) - 1]
        
        else:
            word += event.char
            real_text['text'] = sentence + word

            if event.char == ' ':
                print('result:', word)
                sentence += word
                word = ''

            if event.char == 'Return':
                sentence = ''
                word = ''

        real_text['text'] = sentence + word
 
root = Tk()
root.geometry('300x300')

word = ''
sentence = ''
suggestions = ['the', 'this', 'to']

real_text = Label(root, text="Welcome to the Text Predictor", font = 'Helvetica 16 bold', wraplength = 275, anchor='w')
real_text.pack()

sugg_text = Label(root, text="(1) the   (2) this    (3) to" )
sugg_text.pack()


button = Button (root, text = "Exit", command = close_window)
button.pack()

root.bind('<Key>', get_key)

root.mainloop()
