#! /usr/bin/env python3

import os
import sys
import time
import subprocess as sp
def get_status():
	ret = os.popen("echo $?").read().rstrip()
	return ret

Score = 0
numQuestions = 0
progname = "final_gui.py"
tempFile = "_temp_text_file.txt"
saveFile = 'TestingSaveFile.txt'
valgrindFile = 'valgrind_output.txt'
outFile = "_temp_out_file.txt"

f0 = open(tempFile, "w")
f0.write("This is a temporary text file used for testing.")
time.sleep(1)



print('Testing open and close program (Exit Status):\t\t', end = '')
p = sp.Popen("./" + progname + " -b &> /dev/null", shell = True)
p.communicate()
status = str(p.returncode)
if status == "0":
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)

print('Testing open and close program (Memory):\t\t', end = '')
p = sp.Popen("valgrind --leak-check=full --log-file=" + valgrindFile + " ./" + progname + " -b  &> /dev/null", shell = True)
p.communicate()
time.sleep(1)
f2 = open(valgrindFile, "r")
output = [l for l in f2]
f2.close()
if progname in output[-3]:
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)






print('Testing usage (Exit Status):\t\t', end = '')
#output = os.popen("./" + progname + " -h").read().splitlines()
p = sp.Popen("./" + progname + " -h &> " + outFile, shell = True)
p.communicate()
status = str(p.returncode)

f1 = open(outFile, "r+")
output = [l for l in f1]
f1.close()

if ('Usage' in output[0]) and (status == "0"):
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)

os.popen("rm ./" + outFile)


print('Testing usage (Memory):\t\t', end = '')
p = sp.Popen("valgrind --leak-check=full --log-file=" + valgrindFile + " ./" + progname + " -h  &> " + outFile, shell = True)
p.communicate()
time.sleep(1)
f2 = open(valgrindFile, "r")
output = [l for l in f2]
f2.close()
if progname in output[-3]:
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)







print('Testing learning from file (Exit Status):\t\t', end = '')
os.popen("./" + progname + " -b -f " + tempFile)


p = sp.Popen("./" + progname + " -b -f " + tempFile + " &> /dev/null", shell = True)
p.communicate()
status = str(p.returncode)

if status == "0":
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)



print('Testing learning from file (Memory):\t\t', end = '')
p = sp.Popen("valgrind --leak-check=full --log-file=" + valgrindFile + " ./" + progname + " -b -f " + tempFile + " &> /dev/null", shell = True)
p.communicate()
time.sleep(1)
f2 = open(valgrindFile, "r")
output = [l for l in f2]
f2.close()
if progname in output[-3]:
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)


print('Testing typing a file (Exit Status):\t\t', end = '')
os.popen("./" + progname + " -b -t " + tempFile)
p = sp.Popen("./" + progname + " -b -t " + tempFile + " &> /dev/null", shell = True)
p.communicate()
status = str(p.returncode)
if status == "0":
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)



print('Testing typing a file (Correctness):\t\t', end = '')
os.popen("./" + progname + " -b -t " + tempFile)
p = sp.Popen("diff " + tempFile + " " + saveFile + " &> /dev/null", shell = True)
p.communicate()
status = str(p.returncode)
time.sleep(1)
if status == "0":
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)




print('Testing typing a file (Memory):\t\t', end = '')
p = sp.Popen("valgrind --leak-check=full --log-file=" + valgrindFile + " ./" + progname + " -b -t " + tempFile + " &> /dev/null", shell = True)
p.communicate()
time.sleep(1)
f2 = open(valgrindFile, "r")
output = [l for l in f2]
f2.close()
if progname in output[-3]:
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)


print('Testing changing number of suggestions (Exit Status):\t\t', end = '')
os.popen("./" + progname + " -b -s 8 -t " + tempFile)
p = sp.Popen("./" + progname + " -b -s 8 -t " + tempFile + " &> /dev/null", shell = True)
p.communicate()
status = str(p.returncode)
if status == "0":
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)








print('Testing changing number of suggestions (Correctness):\t\t', end = '')
os.popen("./" + progname + " -b -s 8 -t " + tempFile)
p = sp.Popen("diff " + tempFile + " " + saveFile + " &> /dev/null", shell = True)
p.communicate()
status = str(p.returncode)
time.sleep(1)
if status == "0":
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1
time.sleep(1)




print('Testing changing number of suggestions (Memory):\t\t', end = '')
p = sp.Popen("valgrind --leak-check=full --log-file=" + valgrindFile + " ./" + progname + " -b -s 8 -t " + tempFile + " &> /dev/null", shell = True)
p.communicate()
time.sleep(1)
f2 = open(valgrindFile, "r")
output = [l for l in f2]
f2.close()
if progname in output[-3]:
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1


time.sleep(1)


print('Testing bad arguments (Exit Status):\t\t', end = '')
p = sp.Popen("./" + progname + " these are bad arguments > " + outFile, shell = True)
p.communicate()
status = str(p.returncode)
time.sleep(1)
f1 = open(outFile, "r+")
output = [l for l in f1]
f1.close()
time.sleep(2)
if ("Usage" in output[0]) and (status == "1"):
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1

time.sleep(1)

os.popen("rm ./" + outFile)





print('Testing bad arguments (Memory):\t\t', end = '')
p = sp.Popen("valgrind --leak-check=full --log-file=" + valgrindFile + " ./" + progname + " -f &> /dev/null", shell = True)
p.communicate()
time.sleep(2)
f2 = open(valgrindFile, "r")
output = [l for l in f2]
f2.close()
if progname in output[-3]:
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1

time.sleep(2)



print('Testing bad learning file (Exit Status):\t\t', end = '')
p = sp.Popen("./" + progname + " -f _b_a_d_file.txt > " + outFile, shell = True)
p.communicate()
status = str(p.returncode)
time.sleep(1)
f1 = open(outFile, "r+")
output = [l for l in f1]
f1.close()
time.sleep(2)
if ("File could not be opened" in output[0]) and (status == "1"):
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1

time.sleep(1)




print('Testing bad typing file (Exit Status):\t\t', end = '')
p = sp.Popen("./" + progname + " -t _b_a_d_file.txt > " + outFile, shell = True)
p.communicate()
status = str(p.returncode)
time.sleep(1)
f1 = open(outFile, "r+")
output = [l for l in f1]
f1.close()

time.sleep(2)
if ("File could not be opened" in output[0]) and (status == "1"):
	print("Success")
	Score = Score + 1
else:
	print("Failure")
numQuestions = numQuestions + 1

time.sleep(1)

os.popen("rm ./" + outFile)


f0.close()

#print("Score: " + str(Score))
time.sleep(2)
os.popen("rm ./" + tempFile)
os.popen("rm ./" + valgrindFile)
os.popen("rm ./" + saveFile)
if (Score == numQuestions):
	print("All tests passed")
	exit(0)
else:
	print("Not all tests passed")
	exit(1)

