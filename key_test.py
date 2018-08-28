#! /anaconda3/bin/python3

import sys
import getch
import os
import operator

t = ""

def print_suggestions():
    print("these are suggestions")
   # if len(ret) == 1:
   #     print("1: " + ret[0])
   # if len(ret) == 2:
   #     print("1: " + ret[0] + "\t2: " + ret[1])
   # if len(ret) == 3:
   #     print("1: " + ret[0] + "\t2: " + ret[1] + "\t3: " + ret[2])'''

def get_suggestions(prevWord, word, OurWords, AllWords, InternetWords):
    print("prevWord: " + prevWord + "\tword: " + word)
    ret = []
    if prevWord == "":
        for k in InternetWords:
            if k.startswith(word):
                if k not in ret:
                    ret.append(k)
            if len(ret) == 3:
                return ret
        if len(ret) < 3:
            print(ret)
            return ret

    if prevWord not in OurWords:

        if len(AllWords) > 0:
            sortedAllWords = sorted(AllWords.items(), key = operator.itemgetter(1), reverse=True)
            for i in sortedAllWords:
                if i[0].startswith(word):
                    if i[0] not in ret:
                        ret.append(i[0])
                if len(ret) == 3:
                    print(ret)
                    return ret

        for k in InternetWords:
            if k.startswith(word):
                if k not in ret:
                    ret.append(k)
            if len(ret) == 3:
                print(ret)
                return ret
        if len(ret) < 3:
            print(ret)
            return ret

    sortedOurWords = sorted(OurWords[prevWord].items(), key = operator.itemgetter(1), reverse=True)
    for s in sortedOurWords:
        print(s)

    for i in sortedOurWords:
        if i[0].startswith(word):
            if i[0] not in ret:
                ret.append(i[0])
        if len(ret) == 3:
            print(ret)
            return ret
    if len(AllWords) > 0:
        sortedAllWords = sorted(AllWords.items(), key = operator.itemgetter(1), reverse=True)
        for i in sortedAllWords:
            if i[0].startswith(word):
                if i[0] not in ret:
                    ret.append(i[0])
            if len(ret) == 3:
                print(ret)
                return ret

    for k in InternetWords:
        if k.startswith(word):
            if k not in ret:
                ret.append(k)
        if len(ret) == 3:
            print(ret)
            return ret
    if len(ret) < 3:
        print(ret)
        return ret


def key_pressed():
    global t
    char = getch.getch()
    if char.isdigit() == False:
        t = t + char
    os.system("clear")
    print_suggestions()
    print(t)
    return char

InternetWords = []
InternetWords.append("the")
InternetWords.append("or")
InternetWords.append("and")
AllWords = {}
OurWords = {}

prevWord = ""
word = ""



while True:
    c = key_pressed()
    if c != ' ':
        word = word + c
        get_suggestions(prevWord, word, OurWords, AllWords, InternetWords)
    else:
        print("word: " + word)
  #      if prevWord == "":
  #          AllWords[word] = 1

        if prevWord != "":
            if prevWord in OurWords:
                if word in OurWords[prevWord]:
                    OurWords[prevWord][word] = OurWords[prevWord][word] + 1
                else:
                    OurWords[prevWord][word] = 1
            else:
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
        get_suggestions(prevWord, word, OurWords, AllWords, InternetWords)
        
