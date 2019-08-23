import pygame
import random

gamePoint = 50
dominosPerPlayer = 7

"""
player pseudo-class
	int score
	domino list doms
"""

def shuffleDominos():
	dominos = []

	#load dominos
	l = 6
	while l >= 0:
		r = l
		while r >= 0:
			dominos.append((l, r))
			r -= 1
		l -= 1
	random.shuffle(dominos)
	return dominos

def dominoPips(dom):
	(a, b) = dom
	return a + b
	
def countPips(player):
	(s, d) = player
	t = 0
	for dd in d:
		t += dominoPips(dd)
	return t
	
def hasDouble(player):
	(s, d) = player
	for dd in d:
		(a, b) = dd
		if a == b:
			return True
	return False
	
def highestDouble(player):
	(s, d) = player
	for dd in d:
		(a, b) = dd
		if a == b:
			return a
	return -1

def addDominoToPlayer(player, domino):
	#put domino at end
	player[1].append(domino)
	
	#sort
	index = len(player[1]) - 1
	while index > 0:
		curDom = player[1][index]
		prevDom = player[1][index - 1]
		(curLeft, curRight) = curDom
		(prevLeft, prevRight) = prevDom
		if prevLeft > curLeft:
			break
		if prevLeft == curLeft and prevRight > curRight:
			break
		tempDom = player[1][index]
		player[1][index] = player[1][index - 1]
		player[1][index - 1] = tempDom
		index -= 1
	
def removeDominoFromPlayer(player, index):
	retDom = player[1][index]
	del player[1][index]
	return retDom
	
def addDominoToBoard(player, dIndex, board, side):
	domToAdd = player[1][dIndex]
	if side == 1:
		print "write code for adding to right side"
	else:
		print "write code for adding to left side"
	removeDominoFromPlayer(player, dIndex)
	
def moveIsLegal(player, board, dIndex, side):
	#player = the player whose turn it is
	#board = list of dominoes on the board
	#dIndex = index of domino played
	#side = which side the domino is plaed on
	
	if len(board) == 0:
		return True
	dom = player[1][dIndex]
	if side == 0:
		if dom[0] == board[0] or dom[1] == board[0]:
			return True
		else:
			return False
	else:
		if dom[0] == board[-1] or dom[1] == board[-1]:
			return True
		else:
			return False
			
def canMakeAnyMove(player, board):
	if len(board) == 0:
		return True
	for dIndex in range(len(player[1])):
		for side in range(1):
			if moveIsLegal(player, board, dIndex, side):
				return True
	return False

def playerMakeMove(player, board):
	if not canMakeAnyMove:
		print "no move can be made."
	else:
		validDominoes = []
		for dIndex in range(len(player[1])):
			for side in range(1):
				if moveIsLegal(player, board, dIndex, side):
					validDominoes.append(dIndex)
					print "domino " + `dIndex`,
					if side == 0:
						print "left"
					else:
						print "right"
		while True:
			domSelected = raw_input("enter choice:")
			if domSelected in validDominoes:
				break
			print "Not a valid domino..."
		
		sideSelected = -1
		if not moveIsLegal(player, board, domSelected, 0):
			sideSelected = 1
		if not moveIsLegal(player, board, domSelected, 1):
			sideSelected = 0
		while sideSelected == -1:
			userSide = raw_input("Choose left or right:")
			if userSide == "left":
				sideSelected = 0
			if userSide == "right":
				sideSelected = 1
			if sideSelected == -1:
				print "\"" + userSide + "\" is not a valid choice"
		#here
			
		print "not done"
	
def makeMove(player, board, isFirstMove, method):
	#method: algorithm to make move
	print "not done"
	
			
dominos = shuffleDominos()

players = [(0, []), (0, [])]

if True: #play game
	
	#deal the dominoes
	while not hasDouble(players[0]) and not hasDouble(players[1]):
		print "{\n" + `players` + "\n}\n"
		players = [(0, []), (0, [])]
		for i in range(2 * dominosPerPlayer):
			addDominoToPlayer(players[i / dominosPerPlayer], dominos[i])
		dominos = shuffleDominos()

	turnIndex = 0
	if highestDouble(players[1]) > highestDouble(players[0]):
		turnIndex = 1

	nextFirstTurn = 1 - turnIndex
	
	if True: #play hand

		#print dominos
		for player in players:
			print `player` + "   " + `countPips(player)`
		#players: score, list of dominos

		isDomino = False
		isLocked = False
		
		while not isDomino and not isLocked:
			
			break
		#if nobody has won, deal again, set turn, and flip nextFirstTurn
			
		

print "Done."
