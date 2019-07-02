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
	
	
dominos = shuffleDominos()

players = [(0, []), (0, [])]

while not hasDouble(players[0]) and not hasDouble(players[1]):
	print "{\n" + `players` + "\n}\n"
	players = [(0, []), (0, [])]
	for i in range(2 * dominosPerPlayer):
		addDominoToPlayer(players[i / dominosPerPlayer], dominos[i])
	dominos = shuffleDominos()
	
	
	
	
	
#print dominos
for player in players:
	print `player` + "   " + `countPips(player)`
#players: score, list of dominos

