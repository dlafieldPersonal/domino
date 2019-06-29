# domino

need pygame in order to compile

Tasks:
1. make text based domino game (block)
2. add graphics to game
3. make ai model
4. create ~100? random ai models
5. play-kill-mate-repeat

1. Tasks:
a. make dominoes: 2 sides add to list from 0-0 to 6-6
b. shuffle domino list
c. make 2 players: score & list of dominoes
d. play first round (d1)
e. while neither player has 50 points
f.    play additional round (f1)

d1. Play first round:
i. give each player 7 dominoes
ii. while neither player has a double, take back dominoes, reshuffle and give ea player 7
iii. find which player has highest double and play that domino
iv. set currentturn to other player
v. set nextfirst to other player
vi. continuePlay (d1.vi)

f1. Play additional round:
i. give each player 7 dominoes
ii. set currentturn to nextfirst
iii. toggle nextfirst
iv. let current player choose domino
v. continuePlay (d1.vi)

d1.vi. continuePlay
1. toggle current turn
2. set domino, prevPass, and lock all to False
3. while not domino and not prevPass
4.    if can play
5.       set prevPass to False
6.       ask player to play
7.       remove selected domino from player and add to selected side
8.       if player has no more dominoes, set domino to True
9.    else
10.       if prevPass, set lock to true
11.       else set prevPass to true
12.   toggle current player
13. if domino, count pips and increase score for the other player
14. if lock, count pips for both, calc diff, and increase score of player with fewest pips
15. toggle nextfirst
