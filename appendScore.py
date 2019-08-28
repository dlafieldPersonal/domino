import sys

with open("points.txt", "r") as f:
	pointsList = f.read().splitlines()

players = []
players.append(sys.argv[1])
players.append(sys.argv[2])

with open("scoreHistory.txt", "a") as f:
	if(int(pointsList[0]) > int(pointsList[1])):
		f.write(`players[0]` + "\t" + `pointsList[0]` + "\t" + `players[1]` + "\t" + `pointsList[1]` + "\n")
	else:
		f.write(`players[1]` + "\t" + `pointsList[1]` + "\t" + `players[0]` + "\t" + `pointsList[0]` + "\n")
