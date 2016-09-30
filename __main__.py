from game import Game

def validateInput():
	print ''

def processInput(inputString):
	try:
		size = int(inputString)

		# check size:
		if size < 5:
			print 'Your size is too small. I will pick one for you.'
			return 5
		if size > 16:
			print 'Your size is too big. I will pick one for you.'
			return 16

		return size
	except (TypeError, ValueError):
		# print 'Please enter size between 5 and 16.'
		return None

def main():
	# overture

	while True:
		inputString = raw_input('Airport size (5 - 16): ')
		size = processInput(inputString)
		if size:
			# can play now
			while size < 17:
				Game(size).startPlay()
				print ''
				print '>> WELL DONE >< LEVEL UP <<'
				size += 1
			print '\nYou have completed all levels.'
			print 'You are the BEST commmander!!!'
			return

if __name__ == "__main__":
	main()