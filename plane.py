from numpy import multiply as M
from numpy import add as A
from numpy import subtract as S


ORIENTATIONS  = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INJURY_LEVELS = {0: 'No', 1: 'Minor', 2: 'Severe', 3:'Fatal'}

class Plane:
	
	@classmethod
	def checkCollisionWith(cls, c1, c2):
		return bool(Plane(c1).getPartSet() & Plane(c2).getPartSet())

	def __init__(self, pivot):
		self.parts = {}
		self.spec = {}
		self.build(pivot)

	def getPartSet(self):
		return set(self.spec.keys())

	def build(self, pivot):
		(o, x, y) = pivot
		r = ORIENTATIONS[o] # o[r]ientation
		p = (x, y) # [p]osition
		s = ORIENTATIONS[3 - o] # [s]ide

		chest = p
		head = tuple(A(p, r))
		waist = tuple(S(p, r))
		hip = tuple(S(p, M(2, r)))
		wings = [
			tuple(A(p, s)), 
			tuple(S(p, s)), 
			tuple(A(p, M(2, s))), 
			tuple(S(p, M(2, s)))
		]
		tails = [
			tuple(S(A(p, s), M(2, r))), 
			tuple(S(S(p, s), M(2, r)))
		]

		self.parts['chest'] = chest
		self.parts['head'] = head
		self.parts['waist'] = waist
		self.parts['hip'] = hip
		self.parts['wings'] = wings
		self.parts['tails'] = tails

		self.spec[chest] = 2
		self.spec[head] = 3
		self.spec[hip] = 2
		self.spec[waist] = 2
		for wing in wings:
			self.spec[wing] = 1
		for tail in tails:
			self.spec[tail] = 1
	
	def isThisYourHead(self, coord):
		return self.parts['head'] == coord



