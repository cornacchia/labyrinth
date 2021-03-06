import json
from random import shuffle
from player import Player
from game import Game

print('Labyrinth Game')

numPlayers = 0

while numPlayers <= 0:
  numPlayers = input('Number of players (max 4, "q" to exit): ')

  if (numPlayers == 'q'):
    print('Leaving game')
    break

  try:
    numPlayers = int(numPlayers)
    if (numPlayers > 4):
      print('Too many players, please specify a number <= 4')
      numPlayers = 0
    else:
      print('Start game for', numPlayers, 'players')
      players = []
      for i in range(numPlayers):
        players.append(Player(i))
      with open('treasures.json') as jsonTreasures:
        treasures = json.load(jsonTreasures)
        shuffle(treasures)
        treasureIndex = 0
        for treasure in treasures:
          players[treasureIndex % numPlayers].treasures.append(treasure)
          treasureIndex += 1
        game = Game(players)
        game.start()
  except ValueError:
    print('Cannot read number of players, please insert a valid number')
    numPlayers = 0


