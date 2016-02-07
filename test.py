class moveInput(object):
	def __init__(self,status,)
	
if move.count('e1') == 1 and start[33][-1][-2] == 'K':
		if move.endswith('g1') == True or move.endswith('c1') == True:
			rmove = [move[0:2],move[-2]+ move[-1]]
			s = rmove[0]
			m = rmove[1]
			rmove = [board.check(s),board.check(m)]
			s = rmove[0]
			m = rmove[1]
	
			if  move.endswith('c1') == True and start[25][-1][-1] == 0 and start[17][-1][-1] == 0 and start[9][-1][-1] == 0:
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
			elif move.endswith('g1') == True and start[41][-1][-1] == 0 and start[49][-1][-1] == 0 :
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
	elif move.count('e8') == 1 and start[40][-1][-2] == 'K': 
		if move.endswith('g8') == True or move.endswith('b8') == True: 
			rmove = [move[0:2],move[-2]+ move[-1]]
			s = rmove[0]
			m = rmove[1]
			rmove = [board.check(s),board.check(m)]
			s = rmove[0]
			m = rmove[1]
			if  move.endswith('b8') == True and start[16][-1][-1] == 0 and start[24][-1][-1] == 0 and start[32][-1][-1] == 0:
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
				replace = start[8][-1]
				last_move = start[8][-1]
				back_track = start[32][-1]
				start[8].remove(start[8][-1])
				start[8].append([' ',' ',0])
				start[32].remove(start[32][-1])
				start[32].append(replace)
			
			elif move.endswith('g8') == True and start[48][-1][-1] == 0 and start[56][-1][-1] == 0 :
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
		# I am saving this#############
		#space for options when i get##   
		#to it ########################
		############################### \\\OPTIONS///
		rmove = [move[0:2],move[-2]+ move[-1]]
		s = rmove[0]
		m = rmove[1]
		try:
			rmove = [board.check(s),board.check(m)]
			s = rmove[0]
			m = rmove[1]
		except:
			#move = raw_input('%s your move, I didn\'t understand that last one =>'%player[0])
			move = test(moxi,player[-1])
			rmove = [move[0:2],move[-2]+ move[-1]]
			s = rmove[0]
			m = rmove[1]
			rmove = [board.check(s),board.check(m)]
			s = rmove[0]
			m = rmove[1]
		
		peice = Piece( s, start[s][-1], start)
		pos = peice.pos_handler()
		if pos == False:
			#move = raw_input('%s your move, that last one wasn\'t a real move =>'%player[0])
			move = test(moxi,player[-1])
		
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
					last_move = start[s][-1]
					back_track = start[m][-1]
					p.append(start[m][-1][-2])
					start[s].remove(start[s][-1])
					start[s].append([' ',' ',0])
					start[m].remove(start[m][-1])
					start[m].append(replace)
					king = King(player,start)
					check = king.handler()
					
					if start[m][-1][-2] == 'P' and check == False:
						start[m][-1][0] += 1
						if m % 8 == 1 or m % 8 == 0:
							print 'Congrats your Pawn made it to the other side of the board!'
							an = raw_input('What would you like to be? \n B, H, R, Q >>> ')
							start[m][-1][-2]  = an.capitalize()
							start[m][-1][1] = game.key(start[m][-1])
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
					replace = start[s][-1]
					last_move = start[s][-1]
					back_track = start[m][-1]
					start[s].remove(start[s][-1])
					start[s].append([' ',' ',0])
					start[m].remove(start[m][-1])
					start[m].append(replace)
					king = King(player,start)
					check = king.handler()
					if start[m][-1][-2] == 'P' and check == False:
						if player[-1] == 'white':
							if s % 8 == 5:
								if s + 9 == m:
									start[s+8].remove(start[s+8][-1])
									start[s+8].append([' ',' ',0])
								elif s - 7 == m:
									start[s-8].remove(start[s-8][-1])
									start[s-8].append([' ',' ',0])
						else:	
							if s % 8 == 4:
								if s - 9 == m:
									start[s-8].remove(start[s-8][-1])
									start[s-8].append([' ',' ',0])
								elif s + 7 == m:
									start[s+8].remove(start[s+8][-1])
									start[s+8].append([' ',' ',0])
						
						start[m][-1][0] += 1
						if m % 8 == 1 or m % 8 == 0:
							print 'Congrats your Pawn made it to the other side of the board!'
							 
							an = raw_input('What would you like to be? \n B, H, R, Q >>> ')
							start[m][-1][-2] = an.capitalize()
							start[m][-1][1] = game.key(start[m][-1])
					if check == True:
						start[s].remove(start[s][-1])
						start[s].append(replace)
						start[m].remove(start[m][-1])
						start[m].append(back_track)
						print 'That move puts you in CHECK try again'
						
						break
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
			print moxi,move,peice.possible(),pos,s,m
			print 'You cant move their' 
			
			if turn == 1 :
				turn = 2
			else:
				turn = 1