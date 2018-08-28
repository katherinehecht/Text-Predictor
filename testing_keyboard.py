#! /usr/bin/env python3

import sys
import getch
import os
import operator
import requests
import string
import re
import timeit
from tkinter import *

t = ""

def usage(status=0):
    print(sys.argv[0] + '-f InputFile -s NumberOfSuggestions')
    exit(status)


def print_suggestions(ret):
    for i, r in enumerate(ret):
        print(str(i + 1)  + ": " + str(r))

def get_suggestions_string(ret):
    r2 = ""
    for i, r in enumerate(ret):
        r2 = r2 + str(i + 1)  + ": " + str(r) + "\n"
    return r2


def get_internet_words(word, InternetWords, l):
    ret = []
    for k in InternetWords:
        if k.startswith(word):
            if k not in ret:
                ret.append(k)
        if len(ret) == l:
            return ret
    return ret


def get_all_words(word, AllWords, l):
    ret = []
    if len(AllWords) > 0:
        sortedAllWords = sorted(AllWords.items(), key = operator.itemgetter(1), reverse=True)
        for i in sortedAllWords:
            if i[0].startswith(word):
                if i[0] not in ret:
                    ret.append(i[0])
                if (len(ret) == l):
                    return ret
    return ret


def get_our_words(word, OurWords, l):
    ret = []
    if len(OurWords) > 0:
        sortedOurWords = sorted(OurWords[prevWord].items(), key = operator.itemgetter(1), reverse=True)
        print("In get_our_words")
        print(sortedOurWords)
        for i in sortedOurWords:
            print("List entry: " + str(i))
            if i[0].startswith(word):
                if i[0] not in ret:
                    ret.append(i[0])
                if (len(ret) == l):
                    return ret
    return ret


def handle_no_prevWord(iWords):
    ret = []
    for i in iWords:
        ret.append(i)
    return ret

def handle_not_in_OurWords(aWords, iWords, l):
    ret = []
    for a in aWords:
        ret.append(a)

    if len(ret) < l: 
        for i in iWords:
            ret.append(i)
            if (len(ret) == l):
                return ret
    return ret

def handle_in_OurWords(oWords, aWords, iWords, l):
    print ("In handle_in_OurWorlds")
    ret = []
    for o in oWords:
        ret.append(o)

    if len(ret) < l:
        for a in aWords:
            ret.append(a)
            if len(ret) == l:
                return ret
    if len(ret) < l:
        for i in iWords:
            ret.append(i)
            if len(ret) == l:
                return ret
    return ret


def get_suggestions(prevWord, word, OurWords, AllWords, InternetWords, l):
    print("prevWord: " + prevWord + "\tword: " + word)
    iWords = get_internet_words(word, InternetWords, l)
    if prevWord == "":
        return handle_no_prevWord(iWords)
    
    aWords = get_all_words(word, AllWords, l)
    if prevWord not in OurWords:
        return handle_not_in_OurWords(aWords, iWords, l)
    
    oWords = get_our_words(word, OurWords, l)
    return handle_in_OurWords(oWords, aWords, iWords, l)

def remove_prefix(s, pre):
    if s.startswith(pre):
        return s[len(pre):]
    return s

def strip_punctuation(s):
    return ''.join(ch for ch in s if ch not in string.punctuation)

def key_pressed():
    global t
    char = getch.getch()
    if (char.isdigit() == False) and (ord(char) != 127) and (char != '`'):
        t = t + char
        os.system("clear")
    #  print_suggestions()
        print(t)
        print(str(ord((char))))
    return char


def update_dictionaries():
    global InternetWords
    global AllWords
    global OurWords
    global word
    global prevWord
    print("word: " + word)
    if prevWord != "":
        print("In prevWord != """)
        if prevWord in OurWords:
            print ("prevWord is " + prevWord + " word is: " + word + ".  In the if block")
            if word in OurWords[prevWord]:
                OurWords[prevWord][word] = OurWords[prevWord][word] + 1
            else:
                OurWords[prevWord][word] = 1
        else:
            print ("prevWord is " + prevWord + " word is: " + word + ".  In the else block")
            OurWords[prevWord] = {}
            OurWords[prevWord][word] = 1

    if word in AllWords:
        AllWords[word] = AllWords[word] + 1
    else:
        AllWords[word] = 1
    print("\nAllWords:")
    for q in AllWords:
        print(q + ": " + str(AllWords[q])) 
        
    print("Key: " + word + " Value: " + str(AllWords[word]))
    print("\nOurWords:")
    for p in OurWords:
        for w in OurWords[p]:
            print(p + ": (" + w + ": " + str(OurWords[p][w]) + ")") 
    print("")
    prevWord = word
    word = ""

def save_file():
    global t
    global var3
    global var4
    #f_name = input("Enter file name: ")
    #print('inside save_file')
    var3.set('Enter file name: ')
    root.update_idletasks()
    root.update()

    f_name = ''
    char = getch.getch()
    while (ord(char) != 10):
        print('char just typed was: ' + str(char))
        f_name = f_name + str(char)
        var4.set(f_name)
        root.update_idletasks()
        root.update()
        char = getch.getch()

    if f_name =='':
        print("error")
    else:
        var4.set('')
        print(f_name)
        f = open(f_name, "w")
        f.write(t)
        f.close()
        print('File saved')
        var3.set('Your file is saved in ' + str(f_name))

def read_file():
    global input_file
    global word
    global prevWord
    f = open(input_file, "r")
    iString = ''
    for l in f:
        iString = iString + l
    h = iString.split()
    input_words = [strip_punctuation(word) for word in h]
    print(input_words)
    for i in range(0, len(input_words) - 1):
        print (input_words[i] + ": " + input_words[i+1])
        word = input_words[i+1]
        prevWord = input_words[i]
        update_dictionaries()



URL = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"
InternetWords = requests.get(URL).text.splitlines()
AllWords = {}
OurWords = {}

prevWord = ""
word = ""


numSuggestions = 3







root = Tk()

root.geometry("500x500")

var = StringVar()
var.set('Welcome to our text predictor')
var2 = StringVar()
var2.set('Suggestions')
var3 = StringVar()
var3.set('')
var4 = StringVar()
var4.set('')


l = Label(root, textvariable = var, font = 'Helvetica 16 bold', wraplength = 275, anchor = NW, justify = "left")
l.pack()

l2 = Label(root, textvariable = var2, font = 'Helvetica 16')
l2.pack()

l3 = Label(root, textvariable = var3, font = 'Helvetica 20 bold')
l3.pack()

l4 = Label(root, textvariable = var4, font = 'Helvetica 20 bold')
l4.pack()

input_file = ''












argind = 1
while (argind < len(sys.argv)):
    if (sys.argv[argind] == '-h'):
        usage(0)
    elif (sys.argv[argind] == '-s'):
        argind = argind + 1
        if (argind >= len(sys.argv)):
            usage(1)
        numSuggestions = int(sys.argv[argind])
    elif (sys.argv[argind] == '-f'):
        argind = argind + 1
        if (argind >= len(sys.argv)):
            usage(1)
        input_file = sys.argv[argind]
    argind = argind + 1


if (input_file != ''):
    read_file()

word = ""
prevWord = ""

while True:
    c = key_pressed()
    var3.set('')
    if c == '`':
        save_file()
    elif c != ' ':
        if ord(c) == 127:
            print("inside backspace")
            t = t[:-1]
            word = word[:-1]

            os.system("clear")
            print(t)


        if (not c.isdigit()) and (ord(c) != 127):
            word = word + c
            word = strip_punctuation(word)

        r = get_suggestions(prevWord, word, OurWords, AllWords, InternetWords, numSuggestions)
        print_suggestions(r)
        
        if c.isdigit():
        #    print("inside isdigit")
            if int(c) > len(r):
                continue
            wordToBeTyped = r[int(c) - 1]
            print("wordToBeTyped: " + wordToBeTyped)
            wordToBeTyped = remove_prefix(wordToBeTyped, word)
            t = t + wordToBeTyped + ' '
            os.system("clear")
            print(t)
            word = word + wordToBeTyped
            update_dictionaries()
            #prevWord = word + wordToBeTyped
            #word = ""

        print(str(ord(c)))

    else:
        update_dictionaries()
    r = get_suggestions(prevWord, word, OurWords, AllWords, InternetWords, numSuggestions)
    suggestionString = get_suggestions_string(r) 
    print_suggestions(r)
    var.set(t)
    var2.set(suggestionString)
    root.update_idletasks()
    root.update()

