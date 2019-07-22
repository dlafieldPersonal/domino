import pygame
import random
import collections 

gamePoint = 50
dominosPerPlayer = 7

"""
player pseudo-class
	int score
	domino list doms
"""

"""
board pseudo-class
	int [list] playedDominoes
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
	#assume player has double
	(s, d) = player
	for dd in d:
		(a, b) = dd
		if a == b:
			return a
	
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
	
def addDominoToBoard(board, domino, direction=0):
	#direction = 0 -- put domino on left.  = 1-- put domino on right
	
	if len(board) == 0:
		board.append(domino[0])
		board.append(domino[1])
		return board
		
	if direction == 0:
		board.appendleft(board[0])
		if domino[0] == board[0]:
			board.appendleft(domino[1])
		else:
			board.appendleft(domino[0])
	else:
		board.appendright(board[-1])
		if domino[0] == board[-1]:
			board.append(domino[1])
		else:
			board.append(domino[0])
	return board
	
def printBoard(board):
	if len(board) == 0:
		print "[empty]"
	else:
		for i in range(len(board) / 2):
			print "[" + `board[i * 2]` + `board[i * 2 + 1]` + "]",
		print " "

dominos = shuffleDominos()

players = [(0, []), (0, [])]

board = (collections.deque([]))

#deal dominos for first hand
while not hasDouble(players[0]) and not hasDouble(players[1]):
	print "{\n" + `players` + "\n}\n"
	players = [(0, []), (0, [])]
	for i in range(2 * dominosPerPlayer):
		addDominoToPlayer(players[i / dominosPerPlayer], dominos[i])
	dominos = shuffleDominos()
	
#calculate first player
currentTurnIndex = 0
if not hasDouble(players[0]):
	currentTurnIndex = 1
else:
	if not hasDouble(players[1]):
		currentTurnIndex = 0
	else:
		if highestDouble(players[0]) > highestDouble(players[1]):
			currentTurnIndex = 0
		else:
			currentTurnIndex = 1
			
nextFirst = 1 - currentTurnIndex

#automatically make first move
dIndex = 0
#/***/
#swap players turn
#while not domino and not lock, if can play, then play, swap turn
	
	
	
#print dominos
for player in players:
	print `player` + "   " + `countPips(player)`
#players: score, list of dominos

