import string

from random import shuffle
from random import randint
from random import choice
from random import randrange

from numpy import multiply
from numpy import add
from numpy import subtract

from sets import Set

orientations  = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Game:
	gbW = 10
	gbH = 12

	def __init__(self):
		self.clearGameBoard()
		self.printBoard()

	def printBoard(self):
		print '  ',
		print ' '.join(string.uppercase[0:self.gbW])
		for index, row in enumerate(self.gameBoard):
			print format(index + 1, '02'),
			print ' '.join(['+' if cell == 0 else 'X' for cell in row])
			
	def clearGameBoard(self):
		self.gameBoard = [[0 for i in range(self.gbW)] for j in range(self.gbH)]

	def buildOnePlane(self, pivot):
		return True
		# ori = orientations(:)
		# availableCoord.pop(randrange(len(availableCoord)))
		# (o, x, y) = pivot
		# checkHead = self.gameBoard[x][y] == 0
		# checkLeftWing = 

	def initPlanes(self, numOfPlanes):
		# return an init coord list 
		def initAvailableCoord(): #TBR
			def atCenter(c):
				(o, x, y) = c
				return (x == 3 or x == 4) and (y == 3 or y == 4)

			availableCoord = []

			availableCoord += [(0, x, y) for y in range((2 - 0), self.gbW - (2 - 0)) for x in range(2 - 1, self.gbH - (2 - 0))]

			availableCoord += [(1, x, y) for y in range((2 - 0), self.gbW - (2 - 1)) for x in range(2 - 0, self.gbH - (2 - 0))]

			availableCoord += [(2, x, y) for y in range((2 - 0), self.gbW - (2 - 0)) for x in range(2 - 0, self.gbH - (2 - 1))]

			availableCoord += [(3, x, y) for y in range((2 - 1), self.gbW - (2 - 0)) for x in range(2 - 0, self.gbH - (2 - 0))]

			# optimization
			if self.gbW == 8 and self.gbH == 8:
				availableCoord = list(filter(lambda c: not atCenter(c), availableCoord))

			return availableCoord

		# return new coord list without any conflicts with pivot
		def updateAvailableCoord(availableCoord, pivot):
			# return the shape of the plane as a set of (x,y)
			def populate(c):
				(o, x, y) = c 
				r = orientations[o] # o[r]ientation
				p = (x, y) # [p]osition
				s = orientations[3 - o] # [s]ide

				parts = Set()
				parts.add(p) # chest
				parts.add(tuple(add(p, r))) # head
				parts.add(tuple(subtract(p, r))) # waist
				parts.add(tuple(add(p, s))) # two inner wings
				parts.add(tuple(subtract(p, s))) 
				parts.add(tuple(subtract(p, multiply(2, r)))) # hip
				parts.add(tuple(add(p, multiply(2, s)))) # two outter wings
				parts.add(tuple(subtract(p, multiply(2, s))))
				parts.add(tuple(subtract(add(p, s), multiply(2, r)))) # two tails
				parts.add(tuple(subtract(subtract(p, s), multiply(2, r))))

				return parts
			# eliminate: same position, different orientation 
			def checkConflict(c1, c2):
				return bool(populate(c1) & populate(c2))

			return list(filter(lambda c: not checkConflict(c, pivot), availableCoord))

		availableCoord = initAvailableCoord()

		count = 0
		while count < numOfPlanes:
			# randomly pop a pivot from available coordinates
			pivot = availableCoord.pop(randrange(len(availableCoord)))

			built = self.buildOnePlane(pivot)
			if built:
				count += 1
				availableCoord = updateAvailableCoord(availableCoord, pivot)

		print "Construction Complete: " + str(numOfPlanes) + " planes."

	
	# def getAvailableCoord(self, original, occupiedSpace):
	# 	# 0 -> True, other value -> False
	# 	availableSpace = [[not cell for cell in row]for row in original]
		
	# 	for i, row in enumerate(occupiedSpace):
	# 		for j, cell in enumerate(row):

	# 			# edges
	# 			if i == 0 or i == self.gbH - 1 or j == 0 or j == self.gbW - 1:
	# 				availableSpace[i][j] = False

	# 			# buffers
	# 			if cell: # cell is occupied
	# 				availableSpace[i][j] = False
	# 				# uppper cell:
	# 				if i > 0:
	# 					availableSpace[i - 1][j] = False
	# 				# lower cell:
	# 				if i < self.gbH - 1:
	# 					availableSpace[i + 1][j] = False
	# 				# left cell:
	# 				if j > 0:
	# 					availableSpace[i][j - 1] = False
	# 				# right cell:
	# 				if j < self.gbW - 1:
	# 					availableSpace[i][j + 1] = False
		
	# 	availableCoord = []
	# 	for i, row in enumerate(occupiedSpace):
	# 		for j, cell in enumerate(row):
	# 			if cell:
	# 				availableCoord.append((i,j))
	# 	return availableCoord

	# def buildPlaneOn(self, x, y):
	# 	pass


	# def initOnePlane(self):
	# 	occupied = [[False for i in range(self.gbW)] for j in range(self.gbH)]
	# 	occupied[0][0] = True
	# 	occupied[0][self.gbW - 1] = True
	# 	occupied[self.gbH - 1][0] = True
	# 	occupied[self.gbH - 1][self.gbW - 1] = True 

	# 	availableCoord = self.getAvailableCoord(self.gameBoard, occupied)
	# 	shuffle(availableCoord)

	# 	for (i,j) in availableCoord:
	# 		self.buildPlaneOn(i,j)

	# 	return True


#########

game = Game()
game.initPlanes(3)
