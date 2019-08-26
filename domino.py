import pygame
import random
import sys

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
	print "dIndex = " + `dIndex`
	print "player[1] = " + `player[1]`
	domToAdd = player[1][dIndex]
	if len(board) > 0:
		if side == 1:
			if board[-1] == domToAdd[0]:
				board.append(domToAdd[0])
				board.append(domToAdd[1])
			else:
				board.append(domToAdd[1])
				board.append(domToAdd[0])
		else:
			if board[0] == domToAdd[0]:
				board.insert(0, domToAdd[0])
				board.insert(0, domToAdd[1])
			else:
				board.insert(0, domToAdd[1])
				board.insert(0, domToAdd[0])
	else:
		board.append(domToAdd[0])
		board.append(domToAdd[1])
	removeDominoFromPlayer(player, dIndex)
	
def printBoard(board):
	if len(board) == 0:
		print "{nothing is on the board}"
	else:
		for i in range(len(board)):
			if i % 2 == 0:
				print "[" + `board[i]` + `board[i+1]` + "]",
		print " "
				
def moveIsLegal(player, board, dIndex, side):
	#player = the player whose turn it is
	#board = list of dominoes on the board
	#dIndex = index of domino played
	#side = which side the domino is plaed on
	"""
	print "within moveIsLegal:"
	print "player = " + `player`
	print "board = " + `board`
	print "dIndex = " + `dIndex`
	print "side = " + `side`
	"""
	if len(board) == 0:
		return True
	dom = player[1][dIndex]
	#print "dom = " + `dom`
	if side == 0:
		if dom[0] == board[0] or dom[1] == board[0]:
			return True
		else:
			return False
	else:
		#print "side of board to check is " + `board[-1]`
		if dom[0] == board[-1] or dom[1] == board[-1]:
			return True
		else:
			return False
			
def canMakeAnyMove(player, board):
	if len(board) == 0:
		return True
	for dIndex in range(len(player[1])):
		for side in range(2):
			if moveIsLegal(player, board, dIndex, side):
				return True
	return False

def playerMakeMove(player, board, opponentD):
	if not canMakeAnyMove(player, board):
		print "no move can be made."
	else:
		print "opponent has " + `opponentD` + " dominoes"
		print "board:"
		printBoard(board)
		print "Dominoes:"
		dIndex = 0
		for d in player[1]:
			print `dIndex` + " : " + `d`
			dIndex += 1
		validDominoes = []
		for dIndex in range(len(player[1])):
			#print "checking domino " + `dIndex` + " which is " + `player[1][dIndex]`
			for side in range(2):
				#print "checking side" + `side`
				if moveIsLegal(player, board, dIndex, side):
					validDominoes.append(dIndex)
					print "domino " + `dIndex` + " ",
					if side == 0:
						print "left"
					else:
						print "right"
		while True:
			domSelected = int(raw_input("enter choice: "))
			if domSelected in validDominoes:
				break
			print "Not a valid domino..."
			#doug = 1/0
		
		sideSelected = -1
		if not moveIsLegal(player, board, domSelected, 0):
			sideSelected = 1
		if not moveIsLegal(player, board, domSelected, 1):
			sideSelected = 0
		while sideSelected == -1:
			userSide = raw_input("Choose left or right: ")
			if userSide == "left":
				sideSelected = 0
			if userSide == "right":
				sideSelected = 1
			if sideSelected == -1:
				print "\"" + userSide + "\" is not a valid choice"
		addDominoToBoard(player, domSelected, board, sideSelected)

def highestPipMove(player, board, opponentD):
	print "Choosing highest pip domino..."
	if not canMakeAnyMove(player, board):
		print "The highest pip computer cannot make a move and is forced to pass"
	else:
		highestPip = -1
		domSelected = -1
		sideSelected = ""
		for dIndex in range(len(player[1])):
			for side in range(2):
				if moveIsLegal(player, board, dIndex, side):
					curPips = player[1][dIndex][0] + player[1][dIndex][1]
					if curPips > highestPip:
						highestPip = curPips
						domSelected = dIndex
						sideSelected = side
		addDominoToBoard(player, domSelected, board, sideSelected)

def lowestPipMove(player, board, opponentD):
	print "Choosing lowest pip domino..."
	if not canMakeAnyMove(player, board):
		print "The lowest pip computer cannot make a move and is forced to pass"
	else:
		lowestPip = 99
		domSelected = -1
		sideSelected = ""
		for dIndex in range(len(player[1])):
			for side in range(2):
				if moveIsLegal(player, board, dIndex, side):
					curPips = player[1][dIndex][0] + player[1][dIndex][1]
					if curPips < lowestPip:
						lowestPip = curPips
						domSelected = dIndex
						sideSelected = side
		addDominoToBoard(player, domSelected, board, sideSelected)
	
def highestDoubleMove(player, board, opponentD):
	print "Choosing highest pip double domino..."
	if not canMakeAnyMove(player, board):
		print "The highest pip double computer cannot make a move and is forced to pass"
	else:
		highestPip = -1
		domSelected = -1
		sideSelected = ""
		for dIndex in range(len(player[1])):
			for side in range(2):
				if moveIsLegal(player, board, dIndex, side):
					if player[1][dIndex][0] == player[1][dIndex][1]:
						addDominoToBoard(player, dIndex, board, side)
						return
		highestPipMove(player, board, opponentD)
	
def makeMove(player, board, isFirstMove, method, opponentD):
	#method: algorithm to make move
	boardBefore = len(board)
	if isFirstMove:
		print "player = " + `player`
		#print "len player[1] = " + `len(player[1])`
		for dIndex in range(len(player[1])):
			d = player[1][dIndex]
			if d[0] == d[1]:
				addDominoToBoard(player, dIndex, board, 1)
				break
	else:
		method(player, board, opponentD)
	boardAfter = len(board)
	return boardBefore == boardAfter

models = []
for sysArg in sys.argv[1:]:
	print "this argument = " + `sysArg`
	if sysArg == "high":
		models.append(highestPipMove)
	if sysArg == "low":
		models.append(lowestPipMove)
	if sysArg == "double":
		models.append(highestDoubleMove)
	if sysArg == "player":
		models.append(playerMakeMove)
	if sysArg not in ["high", "low", "double", "player"]:
		print "Load model from file here."
	if len(models) == 2:
		break
	
if len(models) < 2:
	print "Not enough models selected"
	exit(0)
	
dominos = shuffleDominos()
#dominos = [(3, 3), (1, 0), (5, 4), (6, 6), (1, 1), (5, 0), (5, 3), (5, 2), (4, 0), (3, 2), (2, 2), (4, 3), (4, 1), (3, 1), (6, 1), (4, 2), (5, 1), (5, 5), (2, 0), (6, 5), (6, 2), (6, 4), (4, 4), (6, 0), (0, 0), (3, 0), (6, 3), (2, 1)]

print "Dominoes = " + `dominos`
players = [(0, []), (0, [])]

board = []
aWinnerIsFound = False
isFirstHand = True

#if True: #play game
while not aWinnerIsFound: #play game
	
	dominos = shuffleDominos()
	players = [(players[0][0], []), (players[1][0], [])]
	#models = [highestPipMove, highestDoubleMove]
	
	#deal the dominoes
	while not hasDouble(players[0]) and not hasDouble(players[1]):
		print "{\n" + `players` + "\n}\n"
		players = [(players[0][0], []), (players[1][0], [])]
		for i in range(2 * dominosPerPlayer):
			addDominoToPlayer(players[i / dominosPerPlayer], dominos[i])
		dominos = shuffleDominos()
		
	if isFirstHand:
		turnIndex = 0
		if highestDouble(players[1]) > highestDouble(players[0]):
			turnIndex = 1
	else:
		turnIndex = nextFirstTurn

	nextFirstTurn = 1 - turnIndex
	
	board = []
	
	if True: #play hand

		#print dominos
		for player in players:
			print `player` + "   " + `countPips(player)`
		#players: score, list of dominos

		isDomino = False
		isLocked = False
		
		prevPass = makeMove(players[turnIndex], board, isFirstHand, models[turnIndex], len(players[1 - turnIndex][1]))
		isFirstHand = False
		while not isDomino and not isLocked:
			
			print "Board for testing: " + `board`
			for player in players:
				print `player` + "   " + `countPips(player)`
			turnIndex = 1 - turnIndex
			curPass = makeMove(players[turnIndex], board, False, models[turnIndex], len(players[1 - turnIndex][1]))
			if prevPass and curPass:
				isLocked = True
				print "Locked"
			prevPass = curPass
			if len(players[turnIndex][1]) == 0:
				isDomino = True
				print "Domino"

		#if nobody has won, deal again, set turn, and flip nextFirstTurn
	
	player0pips = countPips(players[0])		
	player1pips = countPips(players[1])
	if player0pips < player1pips:
		#player1 has more pips, so player0 scores
		(p, c) = players[0]
		players[0] = (p + player1pips - player0pips, c)
		print "The first player is awarded " + `player1pips - player0pips` + " points for a total of " + `p + player1pips - player0pips`
		if p + player1pips - player0pips >= gamePoint:
			print "The first player has won"
			aWinnerIsFound = True
	else:
		#player0 has more pips, so player1 scores
		(p, c) = players[1]
		players[1] = (p + player0pips - player1pips, c)
		print "The second player is awarded " + `player0pips - player1pips` + " points for a total of " + `p + player0pips - player1pips`
		if p + player0pips - player1pips >= gamePoint:
			print "The second player has won"
			aWinnerIsFound = True
	
	print "----------------"
		
	for player in players:
		print `player` + "   " + `countPips(player)`

print "Done."
