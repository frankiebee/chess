
class Board(object):
	def __init__(self,x):
		self.x = x.lower()
		self.trans = {} # translater
		self.point = {} 
		
		y = 1
		z = 0
		color = 'black'
		for x in xrange(1,65):
			if y > 8: 
				y = 1
			if z == 1:
				color = 'black'
				z = 0
			else:
				color = 'white'
			if x <= 8:
				self.point ['a%d'%y] = [x,z]
	 			self.trans [x] = ['a%d'%x,color]
			elif x > 8  and x < 17:
				self.point ['b%d'%y] = [x, z] 
				self.trans [x] = ['b%d'%y,color] 
			elif x > 16  and x < 25:
				self.point ['c%d'%y] = [x, z] 
				self.trans [x] = ['c%d'%y,color]

			elif x > 24  and x < 33 :
				self.point ['d%d'%y] = [x, z] 
				self.trans [x] = ['d%d'%y,color]
	
			elif x > 32  and x < 41:
				self.point ['e%d'%y] = [x, z] 
				self.trans [x] = ['e%d'%y,color]
	
			elif x > 40  and x < 49:
				self.point ['f%d'%y] = [x, z] 
				self.trans [x] = ['f%d'%y,color]
	
			elif x > 48  and x < 57:
				self.point ['g%d'%y] = [x, z] 
				self.trans [x] = ['g%d'%y,color]
	
			elif x > 56  and x <= 64 :
				self.point ['h%d'%y] = [x, z] 
				self.trans [x] = ['h%d'%y,color]
			
			y += 1
			z += 1
			if x % 8 == 0:
				z = z - 1
			
				
		self.start = self.check()
		
		
	def check(self,x = '' ,option = '',key = 0):
		if x == '':
			x = self.x
		
		if option.lower() == 'color':
			
			return self.point[self.x]
		elif option.lower() == 'key':
			pin = []
			if type(key) == type([0]):
				for x in range(len(key)):
					if type(key[x]) == type([None]):
						key[x] = key[x][0] 
					else:
						pass
					pin.append(self.trans[key[x]])
				return pin
			return self.trans[key]
		
		else:
			return(self.point[x][0])
	
	def visit(self):
		visit = []	
		for x in range(65):
			if x != self.start:
				visit.append(x)
		return visit, 
	
	def legal(self,start ,move):
		if move > 0 and move <= 64:
			if start % 8 == 0 or start % 8 == 7:
				if move % 8 == 1 or move % 8 == 2:
					return False
				else:
					return True
						
			elif start % 8 == 1 or start % 8 == 2:
				if move % 8 == 0 or move % 8 == 7 or move % 8 == 6:
					return False
				else:
					return True							
			else:
				return True
		else:
			return False
	
	def sanity_check(self,x,y):
		check = y.count(x)
		return check
	
	def play(self):
		board = self.trans
		for x in range(1,65):
			if x % 8 == 1 or x % 8 == 2:
				y	= 'white'
			elif x % 8 == 0 or x % 8 == 7:
				y = 'black'
			else:
				y = 0
			if x%8 == 2 or x%8 == 7:
				if y == 'white':
					p = u'\u265F'
				else:
					p = u'\u2659'
				board[x].append([0,p,'P',y])
			elif x == 1 or x == 8 or x == 64 or x == 57: 
				if y == 'white':
					p = u'\u265C'
				else:
					p = u'\u2656'
				board[x].append([0,p,'R',y])
			elif x == 9 or x == 16 or x == 56 or x == 49:
				if y == 'white':
					p = u'\u265E'
				else:
					p = u'\u2658'
				board[x].append([0,p,'H',y])
			elif x == 17 or x == 41 or x == 24 or x == 48:
				if y == 'white':
					p = u'\u265D'
				else:
					p = u'\u2657'
				board[x].append([0,p,'B',y])
			elif x == 25 or x == 32:
				if y == 'white':
					p = u'\u265B'
				else:
					p = u'\u2655'
				board[x].append([0,p,'Q',y])
			elif x == 40 or x == 33:
				if y == 'white':
					p = u'\u265A'
				else:
					p = u'\u2654'
				board[x].append([0,p,'K',y])
			else:
				board[x].append([' ',' ',y])
				
		return board
	
	def go(self,start,move):
		s = self.check(start)
		m = self.check (move)
		if self.leagl(s,m) == true:
			return [s,m]
		else:
			return 'Sory not a legal move'
 
class Piece(object):

	def __init__(self,start,type,game):
		self.start = start
		
		self.type = type
		self.game = game
	def check(self,check):
		pass
	def legal(self,possible,start):
			y = []
			for x in range(len(possible)):
				z = possible[x]
				if z > 0 and z <= 64:
					if start % 8 == 0 or start % 8 == 7:
						if z % 8 != 1 and z % 8 != 2:
							y.append(z)
						
					elif start % 8 == 1 or start % 8 == 2:
						if z % 8 != 0 and z % 8 != 7 and z % 8 != 6:
							y.append(z)							
					else:
						y.append(z)
			
			return y	
	def possible(self):	
		adress = Board('a1')
		if self.type[-2] == 'P':
			if self.start % 8 == 2 and self.type[-1] == 'white':
				a = self.start + 1
				b = self.start + 2
				x = self.start + 9 
				y = self.start - 7
				new = [[a],[b]]
				if x < 65 :
					if self.game[x][-1][-1] != 0 and  self.game[x][-1][-1] != self.type[-1]:
						new.append([x])
				if y > 0:
					if self.game[y][-1][-1] != 0 and  self.game[y][-1][-1] != self.type[-1]:
						new.append([y])
				return new
			elif self.start % 8 == 7 and self.type[-1] == 'black':	
				a = self.start - 1
				b = self.start - 2
				x = self.start - 9 
				y = self.start + 7
				new = [[a],[b]]
				if x > 0 :
					if self.game[x][-1][-1] != 0 and  self.game[x][-1][-1] != self.type[-1]:
						new.append([x])
				if y < 65:
					if self.game[y][-1][-1] != 0 and  self.game[y][-1][-1] != self.type[-1]:
						new.append([y])
				return new
			else:
				if self.type[-1] == 'white':
					x = self.start + 9
					y = self.start - 7
					a = self.start + 1
					b = None
					c = None
					if x <= 64 and self.game[x][-1][-2] != ' ' and self.type[-1] != self.game[x][-1][-1] :
						b = x
					elif x <= 64 and self.game[x][-1][-2] == ' ' and self.start % 8== 5:
						if self.game[self.start + 8][-1][-1] != self.type[-1] and self.game[self.start + 8][-1][0] == 1: 
							b = x
				
					if y > 0:
						if self.game[y][-1][-2] != ' ' and self.type[-1] != self.game[y][-1][-1] :
							c = y
					elif y > 0 and self.game[y][-1][-2] == ' ' and self.start % 8 == 5:
						if self.game[self.start - 8][-1][-1] != self.type[-1] and self.game[self.start - 8][-1][0] == 1: 
							c = y
					r = [a,b,c]
					new =[]
					for x in range(len(r)):
						if r[x] == None:
							pass
						else:
							
							new.append([r[x]])	 
					if len(new) != 0:
						return new
					else:
						return None
				else:
					x = self.start + 7
					y = self.start - 9
					a = self.start - 1
					b = None
					c = None
					if x <= 64 and self.game[x][-1][-2] != ' ' and self.type[-1] != self.game[x][-1][-1] :
						b = x
					elif x <= 64 and self.game[x][-1][-2] == ' ' and self.start % 8 == 4:
						if self.game[self.start + 8][-1][-1] != self.type[-1] and self.game[self.start + 8][-1][0] == 1: 
							b = x
					if y > 0:
						if self.game[y][-1][-2] != ' ' and self.type[-1] != self.game[y][-1][-1] :
							c = y
						elif self.game[y][-1][-2] == ' ' and self.start % 8 == 4:
							if self.game[self.start - 8][-1][-1] != self.type[-1] and self.game[self.start - 8][-1][0] == 1: 
								c = y
					r = [a,b,c]
					new =[]
					for x in range(len(r)):
						if r[x] == None:
							pass
						else:
							new.append([r[x]])	 
					if len(new) != 0:
						return new
					else:
						return None
					  
		elif self.type[-2] == 'R':
			start = self.start + 8
			x = []
			w = []
			y = []
			z = []
			if start <= 64:	
				while start <= 64:
					x.append(start)
					start += 8
			else:
				x = None
			
			start = self.start - 8
			
			if start > 0:
				while start >= 1:
					w.append(start)
					start -= 8
			else:
				w = None
			
			start = self.start + 1
			
			if self.start % 8 != 0:
				while start % 8 != 1:
					y.append(start)
					start += 1
			else:
				y = None
			
			start = self.start - 1
			
			if self.start % 8 != 1:
				while start % 8 != 0:
					z.append(start)
					start -= 1
			else:
				z = None  
			return [x,w,y,z]
					
		elif self.type[-2] == 'H':
			start = self.start
			a = start - 15
			b =	start - 6
			c =	start + 10
			d =	start + 17
			e =	start + 15 
			f =	start + 6
			g =	start - 10
			h =	start - 17 
			posible = [ a, b, h, d, e, f, g, c]
			legal = self.legal(posible,start)
			return [legal]
		
		elif self.type[-2] == 'B':
			
			start = self.start + 9
			x = []
			w = []
			y = []
			z = []
			if start <= 64 and adress.legal(start - 9,start) == True:	
				while start <= 64 and adress.legal(start - 9,start) == True:
					
					x.append(start)
					start += 9
				
			else:
				x = None
			
			start = self.start - 9
			if start > 0 and adress.legal(start + 9,start) == True:
				while start >= 1 and adress.legal(start + 9,start) == True:
					
					w.append(start)
					start -= 9
			else:
				w = None
			start = self.start +7
			if start <= 64 and adress.legal(start - 7,start) == True:	
				while start <= 64 and adress.legal(start - 7,start) == True:
						
					y.append(start)
					start += 7
			else:
				y = None
			start = self.start - 7
			if start > 0 and adress.legal(start + 7,start) == True:
				while start >= 1 and adress.legal(start + 7,start) == True:
					
					z.append(start)
					start -= 7
			else:
				z = None
			
			return [x,w,y,z]
		elif self.type[-2] == 'Q':
			start = self.start + 8
			a = []
			b = []
			c = []
			d = []
			if start <= 64:	
				while start <= 64:
					a.append(start)
					start += 8
			else:
				a = None
			start = self.start - 8
			if start > 0:
				while start >= 1:
					b.append(start)
					start -= 8
			else:
				b = None
			start = self.start + 1
			if self.start % 8 != 0:
				while start % 8 != 1:
					c.append(start)
					start += 1
			else:
				c = None
			start = self.start - 1
			if self.start % 8 != 1:
				while start % 8 != 0:
					d.append(start)
					start -= 1
			else:
				d = None  
			start = self.start + 9
			x = []
			w = []
			y = []
			z = []
			if start <= 64 and adress.legal(self.start,start) == True:	
				
				while start <= 64 and start % 8 != 1:
					x.append(start)
					start += 9
			else:
				x = None
			start = self.start - 9
			if start > 0 and adress.legal(self.start,start) == True:
				while start >= 1 and start % 8 != 0:
					w.append(start)
					start -= 9
			else:
				w = None
			start = self.start +7
			if start <= 64 and adress.legal(self.start,start) == True:	
				while start <= 64 and adress.legal(self.start,start) == True:
					z.append(start)
					start += 7
			else:
				z = None
			start = self.start - 7
			if start > 0 and adress.legal(self.start,start) == True:
				while start >= 1 and adress.legal(self.start,start) == True:
					y.append(start)
					start -= 7
			else:
				y = None
			
			
			return[a,b,c,d,x,w,y,z]
		
		elif self.type[-2] == 'K':
			start = self.start
			a = start + 1
			b = start - 1
			c = start + 7
			d = start - 7
			e = start + 8
			f = start - 8
			g = start + 9
			h = start - 9
			possible = [a,b,c,d,e,f,g,h]
			legal = self.legal(possible,start)
			return [legal]
	def pos_handler(self): 
		pos = self.possible()		
		new =[]
		
		if pos == None:
			return False
		
		for x in range(len(pos)):
			
			if pos[x] == [None]:
				pass
			
			elif self.type[-2] == 'H' or self.type[-2] == 'K' :
				if pos[x] != None:
					for x in range(len(pos[0])):
						check = pos[0][x]
						postion = self.game[check][-1][-2]
						if postion == ' ':
							new.append(check)
						elif self.type[-1] != self.game[check][-1][-1]:		
							new.append(check)	
			else:			
				if pos[x] != None:
					for y in range(len(pos[x])):
						check = pos[x][y]
						postion = self.game[check][-1][-2]
						if postion == ' ':
							new.append(check)
						elif self.type[-1] != self.game[check][-1][-1]:
							if self.type[-2] == 'P':
								if check - 1 == self.start or check - 2 == self.start:
									break
								elif check + 1 == self.start or check + 2 == self.start:
									break
								else:
									new.append(check)
									break
							else:
								new.append(check)
								break
						else:
							break
		
		else:
			return new
	def mov_handler(self):
		pass
		
class King(object):
	def __init__(self,player,game):
		self.king = 0 
		self.game = game
		self.opponent = []
		self.player = player
		self.players_p = [] 
		self.threat = 0
		for x in range(1,65):
			if game[x][-1][-2] == 'K' and game[x][-1][-1] == player[-1]:
				self.king = x
			if  game[x][-1][-1] != player[-1] and game[x][-1][-1] != 0:
				self.opponent.append([x,game[x][-1]])
			if  game[x][-1][-1] == player[-1]:
				self.players_p.append([x,game[x][-1]])
	def handler(self):
		game = self.game
		o = self.opponent
		for x in range(len(o)):
			piece = Piece(o[x][0],o[x][-1],game)	
			pos = piece.pos_handler()
			
			if pos == False:
				pass
			else:
				if pos.count(self.king) == 1:
					self.threat = o[x][0]
					return True   	
		return False  	
			
	def block(self,oppo,type): #opponent peice threatning the king and type
		game = self.game 
		if type[-2] == 'H':
			return False				 
		else:
			opponent = Piece(oppo,type, game)  
			opos = opponent.pos_handler()		
			pace = oppo - self.king
			line = []
			peice = self.players_p
			if pace % 7 == 0:
				pace = 7
			elif pace % 8 == 0:	
				pace = 8
			elif pace % 9 == 0:
				pace = 9
			elif pace % 1 == 0:
				pace = 1 
			opos.sort()
			for a in range(len(opos)):
		 		if pace == 1:
		 			read = oppo + 1
		 			if opos[a] == read:
		 				line.append(opos[a])
		 				read += 1
		 		elif (opos[a] - oppo) % pace == 0:
					line.append(opos[a])
			
			for x in range(len(peice)):	 
				player = Piece(peice[x][0],peice[x][-1], game)
				pos = player.pos_handler()
				if pos != False:
					for y in range(len(line)):
						if pos.count(line[y]) == 1 and peice[x][-1][-2] != 'K':
							return True 
							
			return False 	
	def test(self):
		self.game
	def take(self,oppo):
		game = self.game
		peice = self.players_p
		new = []
		for x in range(len(peice)):
			move = Piece(peice[x][0],peice[x][-1], game)
			pos = move.pos_handler()
			if pos.count(oppo) == 1:
				new.append(peice[x][0])
		if len(new) == 0:
			return False
		else:
			return new	
		return True

	def mate(self,lmove,type): #self, and the move that put in check
		game = self.game
		king = Piece(self.king,game[self.king][-1],game)
		new = []
		re = king.pos_handler()
		for x in range(len(king.pos_handler())):
			new.append(re[x])
		"""
		we see if were in check..
		then if we can take what puts us in check 
		then block 
		then move
	
		"""
		if self.take(lmove) == False:
			
			if self.block(lmove,game[lmove][-1]) == False:
				for x in range(len(self.opponent)):
					o = self.opponent[x]
					op = Piece(o[0],o[-1],game)
					read = king.pos_handler()
					for y in range(len(read)):
						opi = op.pos_handler()
						if o[-1][-2] == 'P':
							if o[-1][-1] == 'white':
								x = o[0] + 9 
								a =	o[0] - 7
							else:	
								x = o[0] - 9 
								a =	o[0] + 7
							opi.append(x)
							opi.append(a)
						if opi.count(read[y]) >= 1:
							try:
								new.remove(read[y])
							except ValueError:
								pass
						 
				if len(new) == 0:
					return True
				else:
					return new
		elif self.take(lmove) != False:
			if len(self.take(lmove)) == 1:
				x = self.take(lmove)
				if self.king == x[0]: 
					replace = game[s][-1]
					last_move = game[s][-1]
					back_track = game[m][-1]
					game[s].remove(game[s][-1])
					game[s].append([' ',' ',0])
					game[m].remove(game[m][-1])
					game[m].append(replace)
					king = King(self.player,game)
					check = king.handler()
					game[s].remove(game[s][-1])
					game[s].append(replace)
					game[m].remove(game[m][-1])
					game[m].append(back_track)
					if check == True:
						
						return True
					
		return self.take(lmove)
				
def test(m,player):
	fuckme = """e2e4
e7e6
d2d4
d7d5
e4e5
c7c5
c2c3
b8c6
g1f3
d8b6
d4c5
b6b2
c1b2
c6e5
f3e5
f8c5
d1d5
e6d5
e5f7
e8f7
b1d2
c5f2
e1f2
f7e8
f2g1
g8f6
f1d3
f6e4
d2e4
d5e4
d3e4
c8e6
e4b7
e6a2
b7a8
a2d5
a8d5
h8f8
a1a7
f8f2
g1f2
e8d8
a7g7
h7h5
f2e3
h5h4
g2g4
h4g3
h2g3
d8e8
h1h7
e8d8
c3c4
d8e8
c4c5
e8d8
g7e7
d8c8
g3g4
c8d8
g4g5
d8c8
g5g6
c8d8
g6g7
d8e7
g7g8

"""
	
	fuckme = fuckme.split('\n')	
	white = []
	black = []
	turn = 1

	for a in range(len(fuckme)):
		fuckme[0:2].append(',')
		if turn == 1:
			white.append(fuckme[a])
			turn = 2
		
		else:
			black.append(fuckme[a])
			turn = 1
	if player == 'black':
		return black[m]
	else:
		return white[m]					
	
class Game(object):
	def __init__(self):
		print """
		Hello! to play a game of chess hit ENTER
		If during the game help is required just 
		type any of the below comands 
		\\\OPTIONS Menue///
		|HELP        : Default will show options , 
		help option will show details on opion
		
		|CHECK	    : shows the peice that puts you in check
		
		|MENUE	    : shows Options menue
		
		"""
		step = raw_input()
	
		self.player_one = [raw_input('player ones name => '),'white']
		self.player_two	= [raw_input('player twos name => '),'black']
	
	def options_menue(self,player,option,game):
		option = option.strip(' ')
		menue = """
		\\\OPTIONS Menue///
		|HELP        : Default will show options , 
		help option will show details on opion
		
		|CHECK	    : shows the peice that puts you in check.
		
		|MENUE		: shows Options menue.
		
		|LAST MOVE  : shows last made move.
		
		|SETINGS 	: ...
		"""
		option = option.upper()
		print option
		if option.find('HELP') == 0:
			space = option.find(' ')
			if space != -1 and space < len(option):
				option_two = option[space+1:len(option)]
				option_two = menue.find(option_two)
				x = menue.find(':',option_two,)
				y = menue.find('.',x)
				print option_two,y
				return option[space+1:len(option)] + menue[x:y].strip(' ')
			else:			
				print menue
				exits = raw_input('HIT ENTER TO EXIT OPTIONS MENUE')
				return 'stop'
		
		elif option == 'CHECK':
			this = King(player,game)
			check = this.handler()
			if check == True:
				return game[this.threat][0],game[this.threat][-1][-3]
			else: 
				return 'You are not in CHECK' 
						
		else: 
		 	return 'continue'	
	
	
	def key(self,thing):
		if thing[-1] == 'black':
			if thing[-2] == 'Q': 
				return u'\u2655'	#queen
			elif thing[-2] == 'R':
				return u'\u2656'	#rook
			elif thing[-2] == 'B':	
				return u'\u2657'	#bbishiop
			elif thing[-2] == 'H':
				return u'\u2658'	#bknigh
		else:	
			if thing[-2] == 'Q':		
				return u'\u265B' #queen	
			elif thing[-2] == 'R':	
				return u'\u265C' # rook	
			elif thing[-2] == 'B':	
				return u'\u265D' #bishiop white	
			elif thing[-2] == 'H':	
				return u'\u265E' #knight white	
	
	def trans(self,move):
		try:
			move = move.strip(' ')
			rmove = [move[0:2],move[-2]+ move[-1]]
			s = rmove[0]
			m = rmove[1]
			rmove = [board.check(s),board.check(m)]
			s = rmove[0]
			m = rmove[1]
		except:
			move = raw_input('%s your move, I didn\'t understand that last one =>'%player[0])
			#move = test(moxi,player[-1]) #### for testing
			rmove = [move[0:2],move[-2]+ move[-1]]
			s = rmove[0]
			m = rmove[1]
			rmove = [board.check(s),board.check(m)]
		return rmove 

def getmove(player):
	move = raw_input('%s your move =>'%player[0])
	while True:
		#move = test(moxi,player[-1])##for testing
		print move
		this = game.options_menue(player,move,start)
		if this != 'continue' and this != 'stop':
			print opponent, 'Captured Pieces %s '%o
			print display
			print 'Captured Pieces %s'%p
			move = raw_input('%s your move %s =>'% (player[0],this))
		elif this == 'stop':
			print opponent, 'Captured Pieces %s '%o
			print display
			print 'Captured Pieces %s'%p
			del sboard
			move = raw_input('%s your move =>'%player[0])
		elif this == 'continue':
			rmove = game.trans(move)
			break			
	return rmove
def show_me(state,type):
	pass 

def update(move,replace,start):
	s = move[0]
	m = move[1]
	start[s].remove(start[s][-1])
	start[s].append([' ',' ',0])
	start[m].remove(start[m][-1])
	start[m].append(replace)
	return start

def back_track(move,rplace,back_track,start):
	s = move[0]
	m = move[1]
	start[s].remove(start[s][-1])
	start[s].append(replace)
	start[m].remove(start[m][-1])
	start[m].append(back_track)	
	return start	

def message(player,status):
	if status == 0:
		return '%r Captured Pieces %s' % (player, p)
	elif status == 1:
		return 'Thats your peice, can\'t move their'
	elif status == 2:
		return 'You cant move their'
	elif status == 3:
		return 'That move puts you in CHECK try again'
	elif status == 4:
		return  '%s YOU ARE IN CHECK!!' %player[0]

board = Board('a1')
game = Game() 
last_move = []
back_track = 0
s = 0 
m = 0
replace = 0
global moxi ## for testing 
moxi = -1 ## for testin
start = board.play() # this is board data
play = [] # not used yet
p1 = game.player_one
p2 = game.player_two
for x in range(1,65):
	play.append([start[x][-1][-2]])
turn = 1
p1_move = 0
p2_move = 0
end = 0
cp1 = ''
cp2 = ''
status = 0

while end != 1:
	sboard = [start[8][-1][1],start[16][-1][1],start[24][-1][1],start[32][-1][1],
    	start[40][-1][1],start[48][-1][1],start[56][-1][1],start[64][-1][1],
    	start[7][-1][1],start[15][-1][1],start[23][-1][1],start[31][-1][1],
    	start[39][-1][1],start[47][-1][1],start[55][-1][1],start[63][-1][1],
    	start[6][-1][1],start[14][-1][1],start[22][-1][1],start[30][-1][1],start[38][-1][1],
    	start[46][-1][1],start[54][-1][1],start[62][-1][1],start[5][-1][1],start[13][-1][1],
    	start[21][-1][1],start[29][-1][1],start[37][-1][1],start[45][-1][1],start[53][-1][1],
    	start[61][-1][1],start[4][-1][1],start[12][-1][1],start[20][-1][1],start[28][-1][1],
    	start[36][-1][1],start[44][-1][1],start[52][-1][1],start[60][-1][1],start[3][-1][1],
    	start[11][-1][1],start[19][-1][1],start[27][-1][1],start[35][-1][1],start[43][-1][1],
    	start[51][-1][1],start[59][-1][1],start[2][-1][1],start[10][-1][1],start[18][-1][1],
    	start[26][-1][1],start[34][-1][1],start[42][-1][1],start[50][-1][1],start[58][-1][1],
    	start[1][-1][1],start[9][-1][1],start[17][-1][1],start[25][-1][1],start[33][-1][1],
    	start[41][-1][1],start[49][-1][1],start[57][-1][1]] # here is the board in raw printing state
	if turn == 2:
		sboard.reverse()
	if turn == 1 :
		display = """
		[8] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[7] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[6] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[5] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[4] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[3] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[2] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[1] |[%s][%s][%s][%s][%s][%s][%s][%s]
		_____________________________
		[-] |[a][b][c][d][e][f][g][h]
		"""% tuple(sboard)
	else:
		display = """
		[1] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[2] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[3] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[4] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[5] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[6] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[7] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[8] |[%s][%s][%s][%s][%s][%s][%s][%s]
		_____________________________
		[-] |[h][g][f][e][d][c][b][a]
		"""% tuple(sboard)
	if turn == 1:
		player = p1 
		p =  cp1
		opponent = p2
		o = cp2
		turn = 2
		moxi += 1
	else:
		player = p2 
		p = cp2
		opponent = p1
		o = cp1
		turn = 1  
	king = King(player,start)
	check = king.handler()
	king.test()
	print opponent, 'Captured Pieces %s '%o
	print display
	if check == True:
		threat = start[king.threat][-1]
		if king.block(m,threat) == True:
			status = 4
			
		else:		
			if king.mate(m,threat) == True:
				print 'GAME OVER %s WINS!' % opponent[0]
				end = 1
				break
			elif king.take(king.threat) != True and king.take(king.threat) != False:
				take = king.take(king.threat)
				if len(take) == 1:
					s = take[0]
					m = king.threat
					change = [s,m]
					replace = start[s][-1]
					last_move = start[s][-1]
					back_track = start[m][-1]
					start = update(change,replace,start)
					king = King(player,start)
					king.player = player
					king.game = start
					check = king.handler()
					start = back_track(change,replace,back_track,start)
					if check == True:
						king = King(player,start)
						retry =	Piece(king.king, start[king.king][-1], start)
						pos = retry.pos_handler()
						if  pos != None:
							c = 0
							for x in range(len(pos)):
								
								s = king.king
								m = pos[x] 
								change = [s,m]
								replace = start[s][-1]
								last_move = start[s][-1]
								back_track = start[m][-1]
								start = update(change,replace,start)
								king = King(player,start)
								king.player = player
								king.game = start
								check = king.handler()
								start = back_track(change,replace,back_track,start)
								if check == True:
									c += 1
							if c == len(pos):
								print 'GAME OVER %s WINS!' % opponent[0]
								end = 1
								break
							else: 
								status = 4
					else:
						status = 4
						
				else:
					mate = king.mate(king.threat,threat)
					
					read = mate
					tally = 0
					for x in range(len(read)):
						king = King(player,start)
						check = king.handler()
						s = mate[x]
						m = king.threat
						change = [s,m]
						replace = start[s][-1]
						last_move = start[s][-1]
						back_track = start[m][-1]
						start = update(change,replace,start)
						king = King(player,start)
						king.player = player
						king.game = start
						check = king.handler()
						
						if check == True:
							tally += 1
						
						start = back_track(change,replace,back_track,start)
						
						
						
					
					if tally == len(read):
						print 'GAME OVER %s WINS!' % opponent[0]
						end = 1
						break
					else:
						status = 4
	
			elif king.take(king.threat) != type(True) and king.take(king.threat) == False:
				mate = king.mate(king.threat,threat)
				read = mate
				tally = 0
				for x in range(len(read)):
					king = King(player,start)
					check = king.handler()
					s = king.king
					m = mate[x]
					change = [s,m]
					replace = start[s][-1]
					last_move = start[s][-1]
					back_track = start[m][-1]
					start = update(change,replace,start)
					king = King(player,start)
					king.player = player
					king.game = start
					check = king.handler()
					
					if check == True:
						tally += 1
						
					start = back_track(change,replace,back_track,start)
					
				if tally == len(read):
					print 'GAME OVER %s WINS!' % opponent[0]
					end = 1
					break
				else:
					status = 4
	
	print message(player,status)
	status = 0
	
	move = getmove(player)
	
	w_castle =[17,49]
	b_castle = [24,56]
	
	if move[0] == 33 and start[33][-1][-2] == 'K' and w_castle.count(move[1]) == 1:
		s = move[0]
		m = move[1]
		if  m == 17 and start[25][-1][-1] == 0 and start[17][-1][-1] == 0 and start[9][-1][-1] == 0:
			replace = start[s][-1]
			last_move = start[s][-1]
			back_track = start[m][-1]
			start[s].remove(start[s][-1])
			start[s].append([' ',' ',0])
			start[m].remove(start[m][-1])
			start[m].append(replace)
			king = King(player,start)
			king.player = player
			king.game = start
			check = king.handler()
	
			if check == True:
				start[s].remove(start[s][-1])
				start[s].append(replace)
				start[m].remove(start[m][-1])
				start[m].append(back_track)
				print 'That move puts you in CHECK try again'
		
				if turn == 1 :
					turn = 2
				else:
					turn = 1 
			replace = start[1][-1]
			last_move = start[1][-1]
			back_track = start[17][-1]
			start[1].remove(start[1][-1])
			start[1].append([' ',' ',0])
			start[17].remove(start[17][-1])
			start[17].append(replace)
		elif m == 49 and start[41][-1][-1] == 0 and start[49][-1][-1] == 0 :
			replace = start[s][-1]
			last_move = start[s][-1]
			back_track = start[m][-1]
			start[s].remove(start[s][-1])
			start[s].append([' ',' ',0])
			start[m].remove(start[m][-1])
			start[m].append(replace)
			king = King(player,start)
			king.player = player
			king.game = start
			check = king.handler()
	
			if check == True:
				start[s].remove(start[s][-1])
				start[s].append(replace)
				start[m].remove(start[m][-1])
				start[m].append(back_track)
				print 'That move puts you in CHECK try again'

				if turn == 1 :
					turn = 2
				else:
					turn = 1 
	
			replace = start[57][-1]
			last_move = start[57][-1]
			back_track = start[41][-1]
			start[57].remove(start[57][-1])
			start[57].append([' ',' ',0])
			start[41].remove(start[41][-1])
			start[41].append(replace)
		else:
			print "Can't castle" 
			if turn == 1 :
					turn = 2
			else:
					turn = 1 
	elif move[0] == 40 and start[40][-1][-2] == 'K' and b_castle.count(move[1]) == 1: 
		s = move[0]
		m = move[1]
		if  m == 24 and start[16][-1][-1] == 0 and start[24][-1][-1] == 0 and start[32][-1][-1] == 0:
			replace = start[s][-1]
			last_move = start[s][-1]
			back_track = start[m][-1]
			start[s].remove(start[s][-1])
			start[s].append([' ',' ',0])
			start[m].remove(start[m][-1])
			start[m].append(replace)
			king = King(player,start)
			king.player = player
			king.game = start
			check = king.handler()
			
			if check == True:
				start[s].remove(start[s][-1])
				start[s].append(replace)
				start[m].remove(start[m][-1])
				start[m].append(back_track)
				print 'That move puts you in CHECK try again'
	
				if turn == 1 :
					turn = 2
				else:
					turn = 1 
			else:	
				replace = start[8][-1]
				last_move = start[8][-1]
				back_track = start[32][-1]
				start[8].remove(start[8][-1])
				start[8].append([' ',' ',0])
				start[32].remove(start[32][-1])
				start[32].append(replace)
		
		elif m == 56 and start[48][-1][-1] == 0 and start[56][-1][-1] == 0 :
			replace = start[s][-1]
			last_move = start[s][-1]
			back_track = start[m][-1]
			start[s].remove(start[s][-1])
			start[s].append([' ',' ',0])
			start[m].remove(start[m][-1])
			start[m].append(replace)
			king = King(player,start)
			king.player = player
			king.game = start
			check = king.handler()
			
			if check == True:
				start[s].remove(start[s][-1])
				start[s].append(replace)
				start[m].remove(start[m][-1])
				start[m].append(back_track)
				print 'That move puts you in CHECK try again'
				
				if turn == 1 :
					turn = 2
				else:
					turn = 1 
			else:
				replace = start[64][-1]
				last_move = start[64][-1]
				back_track = start[48][-1]
				start[64].remove(start[64][-1])
				start[64].append([' ',' ',0])
				start[48].remove(start[48][-1])
				start[48].append(replace)
		else:
			print "Can't castle" 
			if turn == 1 :
					turn = 2
			else:
					turn = 1 
	else:	
		rmove = move
		s = rmove[0]
		m = rmove[1]
	
		peice = Piece( s, start[s][-1], start)
		pos = peice.pos_handler()
		if pos == False:
			print '%s your move, that last one wasn\'t a real move'%player[0]
			#move = test(moxi,player[-1]) ##for testing 
		
			getmove(player)
			s = rmove[0]
			m = rmove[1]
		
		elif pos.count(m) == 1:
			if start[m][-1][-2] == ' ' or start[m][-1][-1] == opponent[1] :
			
				replace = start[s][-1]
				last_move.append(start[s][-1])
				back_track = start[m][-1]
				
				start = update(rmove,replace,start)
				king = King(player,start)
				check = king.handler()
				
				if start[m][-1][-2] == 'P' and check == False:
					if player[-1] == 'white':
						if s % 8 == 5:
							if s + 9 == m and start[s+8][-1][0] == 1:
								start[s+8].remove(start[s+8][-1])
								start[s+8].append([' ',' ',0])
								cp1 = cp1 + start[s+8][-1][-3] + ' '
							elif s - 7 == m and start[s-8][-1][0] == 1:
								start[s-8].remove(start[s-8][-1])
								start[s-8].append([' ',' ',0])
								cp1 = cp1 + start[s-8][-1][-3] + ' '
					else:	
						if s % 8 == 4:
							if s - 9 == m and start[s-8][-1][0] == 1:
								start[s-8].remove(start[s-8][-1])
								start[s-8].append([' ',' ',0])
								cp2 = cp2 + start[s-8][-1][-3] + ' '
							elif s + 7 == m and start[s+8][-1][0] == 1:
								start[s+8].remove(start[s+8][-1])
								start[s+8].append([' ',' ',0])
								cp2 = cp2 + start[s+8][-1][-3] + ' '
					start[m][-1][0] += 1
					if m % 8 == 1 or m % 8 == 0:
						print 'Congrats your Pawn made it to the other side of the board!'
						an = raw_input('What would you like to be? \n B, H, R, Q >>> ')
						start[m][-1][-2]  = an.capitalize()
						start[m][-1][1] = game.key(start[m][-1])
				if check == True:
					start = back_track(rmove,replace,back_track,start)
					status = 3
					if turn == 1 :
						turn = 2
					else:
						turn = 1 
				if back_track[-1] != player[-1]:
					if player[-1] == 'white':
						cp1 = cp1 + back_track[-3] + ' '
					else:
						cp2 = cp2 + back_track[-3] + ' '
				
			else:
				status = 1
				if turn == 1 :
					turn = 2
				else:
					turn = 1 
		else:
			status = 2
			if turn == 1 :
				turn = 2
			else:
				turn = 1
		

