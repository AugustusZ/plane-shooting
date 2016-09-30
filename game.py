from plane import Plane
import plane

import string
from re import findall
from random import randrange
from sets import Set

SCALE = {5:1, 6:1, 7:2, 8:3, 9:4, 10:5, 11:6, 12:8, 13:9, 14:11, 15:13, 16:14}
EMPTY = 0
MISSED = -1
HIT = -2
LABELS = {EMPTY:'+', MISSED: 'X', HIT: '@'}

max_execution_time = 100

class Game:
	def __init__(self, size = 8):
		self.gbW = size
		self.gbH = size

		self.init()
		self.planes = Set()
		self.buildPlanes(SCALE[size])
		self.shotCount = 0

	def printBoard(self, board):
		horizontalMarker = '   ' + ' '.join(string.uppercase[0:self.gbW])
		def getVerticalMarker(index):
			return format(index + 1, '02')

		print ''
		print horizontalMarker
		for index, row in enumerate(board):
			print getVerticalMarker(index),
			print ' '.join([LABELS[cell] if cell < 1 else hex(cell)[2:].upper() for cell in row]),
			print getVerticalMarker(index)
		print horizontalMarker
		print ''
	
	def init(self):
		self.clear()
		self.reportMap = [[EMPTY for i in range(self.gbW)] for j in range(self.gbH)]

	def clear(self):
		# show plane
		self.gameBoard = [[EMPTY for i in range(self.gbW)] for j in range(self.gbH)]
		# show part 
		self.airport = [[EMPTY for i in range(self.gbW)] for j in range(self.gbH)]
		self.planes = Set()

	def generateReport(self, keyword):
		return '[REPORT] ' + str(len(self.planes)) + (' planes' if len(self.planes) > 1 else ' plane') + ' ' + keyword + '.'

	def buildOnePlane(self, pivot, number):
		pl = Plane(pivot)
		self.planes.add(pl)

		for (x, y), injury in pl.spec.iteritems():
			self.airport[x][y] = injury
			self.gameBoard[x][y] = number + 1

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
				return Plane.checkCollisionWith(c1, c2)
			return list(filter(lambda c: not checkConflict(c, pivot), availableCoord))

		availableCoord = initAvailableCoord()

		print '\n===========================\n'
		print '<Reconnaissance Initiated>\n' # actaully it is builind planes...
		# always build exactly numOfPlanes 
		count = 0
		execution_time = 0
		while count < numOfPlanes and execution_time < max_execution_time:
			count = 0
			self.clear()
			availableCoord = initAvailableCoord()
			while count < numOfPlanes:
				# randomly pop a pivot from available coordinates
				pivot = availableCoord.pop(randrange(len(availableCoord)))
				self.buildOnePlane(pivot, count)
				availableCoord = updateAvailableCoord(availableCoord, pivot)
				count += 1
				if not bool(availableCoord):
					break
			execution_time += 1
			print 'Reconnoitering...'

		if count == numOfPlanes:
			print '\n<Reconnaissance Complete>\n' # actually it's 'Construction *'
		else: 
			print '\n<Reconnaissance Failed>\n' # actually it's 'Construction *'
		print self.generateReport('found')

	def processInput(self, inputString):
		try:
			row = int(findall(r'\d+', inputString)[0]) - 1
			col = ord(findall(r'[a-zA-Z]', inputString)[0].upper()) - ord('A')

			# check inside game board boundary:
			if row < 0 or row > self.gbH - 1 or col < 0 or col > self.gbW - 1:
				raise IndexError

			return row, col
		except (TypeError, IndexError):
			pass

	def convertToCoordString(self, coord):
		(row, col) = coord
		return '<' + str(row + 1) + ',' + str(string.uppercase[col]) + '>'

	def destroyPlane(self, coord):
		for pl in self.planes:
			if pl.isThisYourHead(coord):
				for (x, y) in pl.getPartSet():
					self.reportMap[x][y] = HIT
					self.airport[x][y] = EMPTY
					self.gameBoard[x][y] = EMPTY
				self.planes.discard(pl)
				break

	def shootAt(self, coord):
		self.shotCount += 1
		injury = self.airport[coord[0]][coord[1]]
		self.reportMap[coord[0]][coord[1]] = injury if injury > 0 else MISSED

		if injury == max(plane.INJURY_LEVELS.keys()):
			self.destroyPlane(coord)

		return '[REPORT] ' + plane.INJURY_LEVELS[injury] + ' injury on ' + self.convertToCoordString(coord) + '\n' + self.generateReport('left')

	def getHitRate(self):
		return '{:.0%}'.format(SCALE[self.gbW] * 1.0 / self.shotCount)

	def startPlay(self):
		print '\n<Mission Initiated>' 
		while True:
			self.printBoard(self.reportMap)
			inputString = raw_input('Shoot: ')
			coord = self.processInput(inputString)
			if bool(coord):
				print self.shootAt(coord)
				if not bool(self.planes):
					print '<Mission Complete>'
					print '[FINAL REPORT] ' + str(self.shotCount) + (' missiles' if self.shotCount > 1 else ' missile') + ' fired.'
					print '[FINAL REPORT] ' + 'Hit Rate: ' + self.getHitRate()
					print '\n==========================='
					break
				print '\n---------------------------'
			else:
				print 'Bad shot.'



