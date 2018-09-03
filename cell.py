class Cell:
  def __init__(self, exits, player, playerIndex, treasure):
    self.exits = exits
    self.flushPlayers()
    if (playerIndex is not None):
      self.players[playerIndex] = player
    self.treasure = treasure
    self.freeX = -1
    self.freeY = 0

  def rotate(self, times):
    for i in range(times):
      newExits = [0, 0, 0, 0]
      for j in range(len(self.exits)):
        newExits[(j + 1) % len(self.exits)] = self.exits[j]
      self.exits = newExits

  def flushPlayers(self):
    self.players = {0: None, 1: None, 2: None, 3: None}

  def takePlayer(self, playerIndex):
    player = self.players[playerIndex]
    self.players[playerIndex] = None
    return player

  def insertPlayer(self, playerIndex, player):
    self.players[playerIndex] = player

  def hasPlayers(self):
    for player in self.players:
      if player is not None:
        return True
    return False

  # rotate: for each element in exits, assign its value to its index + 1 mod len(exits)