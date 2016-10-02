from time import sleep
import sys
from random import randrange
import words

def slowprint(string = '', breakline = True, pausebetweenchar = True):
	sleep(0.15)
	
	for char in list(string):
		if pausebetweenchar:
			sleep(0.08 if char == ' ' else 0.03)

		sys.stdout.write(char)
		sys.stdout.flush()

	sleep(0.15)

	if breakline:
		print ''

def getGoodJob():
	return words.GOOD[randrange(len(words.GOOD))]

def printGoodJob():
	slowprint(getGoodJob())

