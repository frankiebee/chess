
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
			if z > 1:
				z = 0
				color = 'black'
			if x % 8 == 1:
				self.point ['a%d'%y] = [x,z]
	 			self.trans [x] = ['a%d'%x,color]
			elif x % 8 == 2:
				self.point ['b%d'%y] = [x, z] 
				self.trans [x] = ['b%d'%y,color] 
			elif x % 8 == 3:
				self.point ['c%d'%y] = [x, z] 
				self.trans [x] = ['c%d'%y,color]

			elif x % 8 == 4 :
				self.point ['d%d'%y] = [x, z] 
				self.trans [x] = ['d%d'%y,color]
	
			elif x % 8 == 5:
				self.point ['e%d'%y] = [x, z] 
				self.trans [x] = ['e%d'%y,color]
	
			elif x % 8 == 6:
				self.point ['f%d'%y] = [x, z] 
				self.trans [x] = ['f%d'%y,color]
	
			elif x % 8 == 7:
				self.point ['g%d'%y] = [x, z] 
				self.trans [x] = ['g%d'%y,color]
	
			elif x % 8 == 0 :
				self.point ['h%d'%y] = [x, z] 
				self.trans [x] = ['h%d'%y,color]
		
			
			if x % 8 != 0:
				z += 1
				
				color = 'white'
			else:
				y += 1
		self.start = self.check()
		
		
	def check(self,x = '' ,option = '',key = 0):
		if x == '':
			x = self.x
		else:
			x = x
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
				if move % 8 != 1 and move % 8 != 2:
					return True
				else:
					return False
						
			elif start % 8 == 1 or start % 8 == 2:
				if move % 8 != 0 and move % 8 != 7 and move % 8 != 6:
					return True
				else:
					return False							
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
				board[x].append([0,'P',y])
			elif x == 1 or x == 8 or x == 64 or x == 57: 
				 board[x].append(['R',y])
			elif x == 9 or x == 16 or x == 56 or x == 49:
				 board[x].append(['H',y])
			elif x == 17 or x == 41 or x == 24 or x == 48:
				 board[x].append(['B',y])
			elif x == 25 or x == 32:
				 board[x].append(['Q',y])
			elif x == 33 or x == 40:
				 board[x].append(['K',y])
			else:
				 board[x].append([' ',y])
				
		return board
	
	def go(self,start,move):
		s = self.check(start)
		m = self.check (move)
		if self.leagl(s,m) == true:
			return [s,m]
		else:
			return 'Sory not a legal move'
class Game(object):
	def __init__(self):
		self.player_one = [raw_input('player ones name => '),'white']
		self.player_two	= [raw_input('player twos name => '),'black']
	
			 
class Piece(object):

	def __init__(self,start,type,game):
		self.start = start
		
		self.type = type
		self.game = game
	def check(self,check):
		pass
	def legal(self,possible,start=0):
			y = []
			start = start
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
			if self.start % 8 == 2:
				a = self.start + 1
				b = self.start + 2
				return [[a],[b]]
			elif self.start % 8 == 7 and self.type[-1] == 'black':	
				a = self.start - 1
				b = self.start - 2
				return [[a],[b]]
			else:
				if self.type[-1] == 'white':
					x = self.start + 9
					y = self.start - 7
					a = self.start + 1
					b = None
					c = None
					if self.game[x][-1][-2] != ' ' and self.type[-1] != self.game[x][-1][-1] :
						b = x
					else:
						pass
				
					if y > 0:
						if self.game[y][-1][-2] != ' ' and self.type[-1] != self.game[y][-1][-1] :
							c = x
					else:
						pass
					r = [a,b,c]
					new =[]
					for x in range(len(r)):
						if r[x] == None:
							pass
						else:
							new.append([r[x]])	 
					return new
				else:
					x = self.start - 9
					y = self.start + 7
					a = self.start - 1
					b = None
					c = None
					if x > 0 and self.game[x][-1][-2] != ' ' and self.type[-1] != self.game[x][-1][-1] :
						b = x
					else:
						pass
				
					if self.game[y][-1][-2] != ' ' and self.type[-1] != self.game[y][-1][-1] :
						c = x
					else:
						pass
					r = [a,b,c]
					new =[]
					for x in range(len(r)):
						if r[x] == None:
							pass
						else:
							new.append([r[x]])	 
					return new
					  
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
			
			if start <= 64 and adress.legal(self.start,start) == True:	
				while start <= 64:
					x.append(start)
					start += 9
			else:
				x = None
			start = self.start - 9
			if start > 0:
				while start >= 1:
					w.append(start)
					start -= 9
			else:
				w = None
			start = self.start +7
			if start <= 64 and adress.legal(self.start,start) == True:	
				while start <= 64:
					y.append(start)
					start += 7
			else:
				y = None
			start = self.start - 7
			if start > 0 and adress.legal(self.start,start) == True:
				while start >= 1:
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
				while start <= 64:
					x.append(start)
					start += 9
			else:
				x = None
			start = self.start - 9
			if start > 0 and adress.legal(self.start,start) == True:
				while start >= 1:
					w.append(start)
					start -= 9
			else:
				w = None
			start = self.start +7
			if start <= 64 and adress.legal(self.start,start) == True:	
				while start <= 64:
					z.append(start)
					start += 7
			else:
				z = None
			start = self.start - 7
			if start > 0 and adress.legal(self.start,start) == True:
				while start >= 1:
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
			
			if pos[x] == None:
				pass
			elif pos[x] != [None]:
				for y in range(len(pos[x])):
					check = pos[x][y]
					postion = self.game[check][-1][-2]
					if postion == ' ':
						new.append(check)
					elif self.type[-1] != self.game[check][-1][-1]:
						if self.type[-2] == 'P' and pos[x][y] - 1 == self.start:
							break
						else:
							new.append(check)
							break
					else:
						break
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
			piece = Piece(self.opponent[x][0],self.opponent[x][-1],game)	
			pos = piece.pos_handler()
			
			if pos == False:
				pass
			else:
				if pos.count(self.king) == 1:
					return True   	
		return False  	
	
	def mate(self):
		piece = Piece(self.king,self.game[self.king][-1],self.game)
		o = self.opponent
		check = []
		king = peice.pos_handler()
		
		if king == False:
			return True
		else:
			for x in range(len(king)):
				for y in range(len(o)):
					opponent = Piece(self.opponent[y][0],self.opponent[y][-1],self.game)  
					pos = opponent.pos_handler()
			
					if pos == False:
						pass
					else:
						if pos.count(king[x]) == 1:
							check.append(1)
							break   	
		if len(king) == len(check):
			return True
		else:	
			return False
			
	def block(self,oppo,type): #opponent peice threatning the king and type
		if type[-2] == 'H':
			return False 
		else:
		
			opponent = Piece(oppo,type,self.game)  
			opos = opponent.pos_handler()		
			pace = oppo - self.king
			line = []
			peice = self.players_p
			if pace % 1 == 0:
				pace = 1 
			elif pace % 7 == 0:
				pace = 7
			elif pace % 8 == 0:	
				pace = 8
			elif pace % 9 == 0:
				pace = 9
		
			for x in range(len(opos)):
				if (opos[x] - oppo) % pace == 0:
					line.append(opos[x])
		 
			for x in range(len(peice)):	 
				player = Piece(peice[x][0],peice[x][-1],self.game)
				pos = player.pos_handler()
				
				if pos != False:
					for y in range(len(line)):
						if pos.count(line[y]) == 1:
							return True 
			return False 	

board = Board('a1')
game = Game() 
last_move = []
m = 0
start = board.play()
play = []
p1 = game.player_one
p2 = game.player_two
for x in range(1,65):
	play.append([start[x][-1][-2]])
turn = 1
p1_move = 0
p2_move = 0
end = 0
cp1 = []
cp2 = []
 

while end != 1:
	sboard = [start[8][-1][-2],start[16][-1][-2],start[24][-1][-2],start[32][-1][-2],
    	start[40][-1][-2],start[48][-1][-2],start[56][-1][-2],start[64][-1][-2],
    	start[7][-1][-2],start[15][-1][-2],start[23][-1][-2],start[31][-1][-2],
    	start[39][-1][-2],start[47][-1][-2],start[55][-1][-2],start[63][-1][-2],
    	start[6][-1][-2],start[14][-1][-2],start[22][-1][-2],start[30][-1][-2],start[38][-1][-2],
    	start[46][-1][-2],start[54][-1][-2],start[62][-1][-2],start[5][-1][-2],start[13][-1][-2],
    	start[21][-1][-2],start[29][-1][-2],start[37][-1][-2],start[45][-1][-2],start[53][-1][-2],
    	start[61][-1][-2],start[4][-1][-2],start[12][-1][-2],start[20][-1][-2],start[28][-1][-2],
    	start[36][-1][-2],start[44][-1][-2],start[52][-1][-2],start[60][-1][-2],start[3][-1][-2],
    	start[11][-1][-2],start[19][-1][-2],start[27][-1][-2],start[35][-1][-2],start[43][-1][-2],
    	start[51][-1][-2],start[59][-1][-2],start[2][-1][-2],start[10][-1][-2],start[18][-1][-2],
    	start[26][-1][-2],start[34][-1][-2],start[42][-1][-2],start[50][-1][-2],start[58][-1][-2],
    	start[1][-1][-2],start[9][-1][-2],start[17][-1][-2],start[25][-1][-2],start[33][-1][-2],
    	start[41][-1][-2],start[49][-1][-2],start[57][-1][-2]]
	if turn == 2:
		sboard.reverse()
	else:
		pass
	if turn == 1 :
		display = """
		[h] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[g] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[f] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[e] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[d] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[c] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[b] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[a] |[%s][%s][%s][%s][%s][%s][%s][%s]
		_____________________________
		[-] |[1][2][3][4][5][6][7][8]
		"""% tuple(sboard)
	else:
		display = """
		[a] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[b] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[c] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[d] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[e] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[f] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[g] |[%s][%s][%s][%s][%s][%s][%s][%s]
		[h] |[%s][%s][%s][%s][%s][%s][%s][%s]
		_____________________________
		[-] |[8][7][6][5][4][3][2][1]
		"""% tuple(sboard)
	if turn == 1:
		player = p1 
		p =  cp1
		opponent = p2
		o = cp2
		turn = 2
	else:
		player = p2 
		p = cp2
		opponent = p1
		o = cp1
		turn = 1  
	
	king = King(player,start)
	check = king.handler()
	print opponent, 'Captured Pecies %r'%o
	print display
	
	if check == True:
		if king.block(m,last_move) == True:
			print '%s YOU ARE IN CHECK!!' %player[0]
		else:
			if king.mate() == True:
				print 'GAME OVER %s WINS!' % opponent[0]
				end = 1
				break
			else:
				print '%s YOU ARE IN CHECK!!' %player[0]
	else:
		print player, 'Captured Pecies %r'%p
	move = raw_input('%s your move =>'%player[0])
	rmove = [move[0:2],move[-2]+ move[-1]]
	s = rmove[0]
	m = rmove[1]
	rmove = [board.check(s),board.check(m)]
	s = rmove[0]
	m = rmove[1]
	
	peice = Piece( s, start[s][-1], start)
	pos = peice.pos_handler()
	
	if pos == False:
		move = raw_input('%s your move, that last one wasn\'t a real move =>'%player[0])
		rmove = [move[0:2],move[-2]+ move[-1]]
		s = rmove[0]
		m = rmove[1]
		rmove = [board.check(s),board.check(m)]
		s = rmove[0]
		m = rmove[1]
	
	if pos.count(m) == 1:
		if start[m][-1][-2] == ' ' or start[m][-1][-1] == opponent[1] :
			
			if start[m][-1][-1] == opponent[1]:
				
				replace = start[s][-1]
				back_track = start[m][-1]
				p.append(start[m][-1][-2])
				start[s].remove(start[s][-1])
				start[s].append([' ',0])
				start[m].remove(start[m][-1])
				start[m].append(replace)
				king = King(player,start)
				check = king.handler()
				
				if check == True:
					p.remove(p[-1])
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
					if start[m][-1][-2] == 'P':
						start[m][-1][0] += 1
						if start[m][-1][0] == 6:
							print 'Congrats your Pawn made it to the other side of the board!'
							start[m][-1][-2] = raw_input('What would you like to be? \n B H R Q >>>')
			else:
				replace = start[s][-1]
				last_move = start[s][-1]
				back_track = start[m][-1]
				start[s].remove(start[s][-1])
				start[s].append([' ',0])
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
			print 'Thats your peice, can\'t move their'
			if turn == 1 :
				turn = 2
			else:
				turn = 1 
	else:
		print 'You cant move their' 
		if turn == 1 :
			turn = 2
		else:
			turn = 1
	
	
