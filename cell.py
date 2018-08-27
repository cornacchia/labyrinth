# must have a rotate method
class Cell:
  def __init__(self, exits, player, treasure):
    self.exits = exits
    self.player = player
    self.treasure = treasure
    self.freeX = -1
    self.freeY = 0

  def rotate(self, times):
    for i in range(times):
      newExits = [0, 0, 0, 0]
      for j in range(len(self.exits)):
        newExits[(j + 1) % len(self.exits)] = self.exits[j]
      self.exits = newExits

  # rotate: for each element in exits, assign its value to its index + 1 mod len(exits)