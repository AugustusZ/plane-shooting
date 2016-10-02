from game import Game
from printer import slowprint
from printer import printGoodJob
import words
import stopwatch

def processInput(inputString):
	try:
		size = int(inputString)

		# check size:
		if size < 1:
			slowprint('It seems like you are a newbie here.')
			slowprint('Now you have Clearance Level 1, the lowest level.')
			return 1
		if size > 12:
			slowprint("Don't overestimate yourself, Agent K.")
			slowprint('Now you have Clearance Level 12, the highest level an agent can get.')
			return 12

		return size
	except (TypeError, ValueError):
		# print 'Please enter size between 5 and 16.'
		return None

def main():
	slowprint('Nice to meet you, Agent K!')

	while True:
		slowprint('Enter your Clearance Level (1 - 12):', breakline = False)
		inputString = raw_input(' ')
		level = processInput(inputString)
		if level:
			# can play now
			startGameTime = stopwatch.now()
			
			while level < 13: 
				size  = level + 4
				
				Game(size).startPlay()
				
				level += 1
				slowprint()
				printGoodJob()
				slowprint('Now you have Clearance Level ' + str(level))
			
			endGameTime = stopwatch.now()

			slowprint('\nYou have completed all missions.')
			slowprint('Total Elapsed Time: ' + stopwatch.diffTime(endGameTime, startGameTime))
			slowprint('Thank you, Agent K (CL: 13).')
			slowprint('\n############## END ##############\n')
			return

if __name__ == "__main__":
	main()