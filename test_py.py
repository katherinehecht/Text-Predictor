#! /usr/bin/env python3


import sys
sys.path.insert(0, '__PATH_TO_LATEST_KEYBOARD_VERSION__')
def readboard():
	import keyboard
	keyboard.press_and_release('shift+s, space')
	keyboard.wait()
	keyboard.write('Hello')
	keyboard.wait()
readboard
