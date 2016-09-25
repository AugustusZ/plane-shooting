import string
from random import shuffle
from random import randint
from random import choice
from random import randrange
from numpy import multiply
from numpy import add
from numpy import subtract
from sets import Set
from copy import deepcopy

orientations  = [(-1, 0), (0, 1), (1, 0), (0, -1)]
scale = {5:1, 6:2, 7:2, 8:3, 9:4, 10:5, 11:6, 12:8, 13:9, 14:11, 15:13, 16:14}
EMPTY = 0

max_execution_time = 100

class Game:
	def __init__(self, size):
		self.gbW = size
		self.gbH = size
		self.clearGameBoard()
		self.buildPlanes(scale[size])

	def printBoard(self):
		print '  ',
		print ' '.join(string.uppercase[0:self.gbW])
		for index, row in enumerate(self.gameBoard):
			print format(index + 1, '02'),
			print ' '.join([' ' if cell == EMPTY else str(cell) for cell in row])
		print ''
			
	def clearGameBoard(self):
		self.gameBoard = [[EMPTY for i in range(self.gbW)] for j in range(self.gbH)]

	# return the shape of the plane as a set of (x,y)
	def populate(self, c):
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

	def buildOnePlane(self, pivot, number):
		for (x, y) in self.populate(pivot):
			self.gameBoard[x][y] = number

	def buildPlanes(self, numOfPlanes):
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
			def checkConflict(c1, c2):
				return bool(self.populate(c1) & self.populate(c2))
			return list(filter(lambda c: not checkConflict(c, pivot), availableCoord))

		availableCoord = initAvailableCoord()

		#
		print "building . .",
		# always build exactly numOfPlanes 
		count = 0
		execution_time = 0
		while count < numOfPlanes and execution_time < max_execution_time:
			count = 0
			self.clearGameBoard()
			availableCoord = initAvailableCoord()
			while count < numOfPlanes:
				# randomly pop a pivot from available coordinates
				pivot = availableCoord.pop(randrange(len(availableCoord)))
				self.buildOnePlane(pivot, count + 1)
				availableCoord = updateAvailableCoord(availableCoord, pivot)
				count += 1
				if not bool(availableCoord):
					break
			execution_time += 1
			print '.',
		print ""
		self.printBoard()
		if count == numOfPlanes:
			print "<Construction Complete> (" + str(execution_time) + ")",
		else: 
			print "<Construction Failed>",
		print str(count) + "/" + str(numOfPlanes)

game = Game(8)

