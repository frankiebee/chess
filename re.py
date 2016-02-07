class test(object):
	def __init__(self):
		self.red = raw_input('test')
	def plus(self):
		def __init__(self):
		
		red
			

test = test()

print test.plus.red()



def move(self, m):
		pace = m - self.king
		if pace == 0:
			return False
		line = []
		if pace % 7 == 0:
			pace = 7
		elif pace % 8 == 0:	
			pace = 8
		elif pace % 9 == 0:
			pace = 9
		elif pace % 1 == 0:
			pace = 1 
		super_broken = 0
		fake = {self.king:['Q',self.player[-1]]}
		piece = Piece(self.king,['Q',self.player[-1]],self.game)
		pos = piece.possible()
		for x in range(len(pos)):
			if super_broken == 1:
				break
			if pos[x] != None:
				for y in range(len(pos[x])):
					if pos[x][y] % pace == 0:
						if self.game[pos[x][y]][-1][-1] == 0:
							line.append(pos[x][y])
						elif pos[x][y] == m:
							line.append(pos[x][y])
						else:
							line.append(pos[x][y])
							super_broken = 1
							break
		threat = self.game[line[-1]]
		if threat[-1][-1] == 0:
			return True # yes you can move you are not in danger
		elif threat[-1][-1] != self.player[-1]:
			if threat[-1][-2] == 'R' or threat[-1][-2] == 'B':
				if threat[-1][-2] == 'R' and pace == 1 or pace == 8:
					return False
				elif threat[-1][-2] == 'B' and pace == 7 or pace == 9:
					return False
				elif threat[-1][-2] == 'Q':
					return False
		elif threat[-1][-1] == player[-1]:
			return False