#! /usr/bin/env python3

#Katherine Hecht, Julia Hughes, Richard Stefanik
import os
import time

#titles = ["Alice in Wonderland", "Beowulf", "The Jungle Book"]
#fileNames = ["input_wonderland.txt", "input_beowulf.txt", "input_jungle.txt"]
#BACKENDS = ["unsorted", "sorted", "bst", "rbtree", "treap", "unordered", "chained", "open"]

URL = 'http://www.gutenberg.org/files/'
secondURL = 'http://www.gutenberg.org/cache/epub/'


fileNums = [2542]
fileNames = ["lyrics.txt", "7oldsamr.txt", "advtthum.txt", "BillOfRights.txt"]


'''for i, f in enumerate(fileNums):
    content = URL + str(f) + "/" + str(f) + "-0.txt"
    command = "curl -sL " + content + " > " + fileNames[i]
    print(command)
    os.popen(command)
    command = "head -n 1 " + fileNames[i]
    print(command)
    output = os.popen(command).read()
    print(output)
    if "404 Not Found" in output:
    content = secondURL + str(f) + "/pg" + str(f) + ".txt"
    command = "curl -sL " + content + " > " + fileNames[i]
    print(command)
    os.popen(command)'''

pythonPath = os.popen("which python3").read().rstrip()
print(pythonPath)

programName = './final_gui.py'

oFile = open("table.txt", "w")

head =  "| Text             |   File Size  | Number of Suggestions | Time to Learn | Memory to Learn | Time to Type    | Memory to Type |"
blank = "|------------------|--------------|-----------------------|---------------|-----------------|-----------------|----------------|"
print(head)
print(blank)
oFile.write(head + "\n")
oFile.write(blank + "\n")

suggestions = 8
for i, f in enumerate(fileNames):
    for s in range(suggestions):
        command = "./measure " + pythonPath + " " + programName + " -b -f " + f + " -s " + str(s + 1)
       # command = "./measure " + pythonPath + " " + programName + " -b -f " + f + " -s " + str(s + 1)
        #print(command)
        output = os.popen(command).read().splitlines()[-1]
        time_elapsed = output.split("\t")[0].split(" ")[0]
        memory_usage = output.split("\t")[1].split(" ")[0]
        timeToLearn = time_elapsed
        memoryToLearn = memory_usage

        command = "./measure " + pythonPath + " " + programName + " -b -t " + f + " -s " + str(s + 1)
        #print(command)
        output = os.popen(command).read().splitlines()[-1]
        time_elapsed = output.split("\t")[0].split(" ")[0]
        memory_usage = output.split("\t")[1].split(" ")[0]
        timeToType = time_elapsed
        memoryToType = memory_usage

        #command = "ls -lh | grep " + f + " | cut -d \" \" -f 9"
        #fileSize = os.popen(command).read().rstrip()
        fileSize = str(os.stat(f).st_size / 1000)

        oString = "|{:18}|{:>11} Kb|{:>23}|{:>13.7} s|{:>14.7} Mb|{:>15.7} s|{:>13.7} Mb|".format(fileNames[i], str(fileSize), str(s + 1), timeToLearn, memoryToLearn, timeToType, memoryToType)
        print(oString)
        oFile.write(oString + "\n")

for i in fileNames:
    command = "rm ./" + i
  #  os.popen(command)


oFile.close()
