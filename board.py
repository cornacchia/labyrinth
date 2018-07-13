import json
from random import shuffle
from random import randint
from cell import Cell

treasures = [
  'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h',
  'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p',
  'q', 'r', 's', 't',
  'u', 'v', 'w', 'x'
]

# must have a cells[][] and a out_piece
class Board:
  def __init__(self, players):
    self.freeCell = None
    self.players = players
    # import cells definitions
    with open('cell-definition.json') as cellsDefinition:
      self.cellsDefinition = json.load(cellsDefinition)
    # create empty board
    self.cells = self.createBlankCells()
    # set fixed cells
    self.setFixedCells()
    # set other cells in randomized order
    self.nonFixedCells = self.cellsDefinition['nonFixedCells']
    shuffle(self.nonFixedCells)
    self.setOtherCells()

  def createBlankCells(self):
    cells = [[] for i in range(7)]
    for cell in cells:
      for i in range(7):
        cell.append(None)
    return cells

  def setFixedCells(self):
    # set player starting points
    for i in range(len(self.players)):
      playerStartingPoint = self.cellsDefinition['playerStartingPoints'][i]
      newCell = Cell(playerStartingPoint['exits'], self.players[i], None)
      self.cells[playerStartingPoint['position'][0]][playerStartingPoint['position'][1]] = newCell
    # set other starting points
    for i in range(len(self.players), len(self.cellsDefinition['playerStartingPoints'])):
      emptyStartingPoint = self.cellsDefinition['playerStartingPoints'][i]
      newCell = Cell(emptyStartingPoint['exits'], None, None)
      self.cells[emptyStartingPoint['position'][0]][emptyStartingPoint['position'][1]] = newCell
    # set other fixed cells
    for i in range(len(self.cellsDefinition['fixedCells'])):
      fixedCellDefinition = self.cellsDefinition['fixedCells'][i]
      newCell = Cell(fixedCellDefinition['exits'], None, treasures[i])
      self.cells[fixedCellDefinition['position'][0]][fixedCellDefinition['position'][1]] = newCell

  def setOtherCells(self):
    otherCells = []
    treasure = 12
    for i in range(self.cellsDefinition['ninetyDegreesTreasureCells']):
      newCell = Cell([1, 1, 0, 0], None, treasures[treasure])
      treasure += 1
      otherCells.append(newCell)
    for i in range(self.cellsDefinition['ninetyDegreesCells']):
      newCell = Cell([1, 1, 0, 0], None, None)
      otherCells.append(newCell)
    for i in range(self.cellsDefinition['threeExitsCells']):
      newCell = Cell([1, 1, 1, 0], None, treasures[treasure])
      treasure += 1
      otherCells.append(newCell)
    for i in range(self.cellsDefinition['corridors']):
      newCell = Cell([1, 0, 1, 0], None, None)
      otherCells.append(newCell)

    shuffle(otherCells)
    for i in range(len(otherCells)):
      cell = otherCells[i]
      cell.rotate(randint(0, 3))
      if i < len(self.nonFixedCells):
        # insert at nonFixedCells[i] position
        x = int(self.nonFixedCells[i][0])
        y = int(self.nonFixedCells[i][1])
        self.cells[x][y] = cell
      else:
        self.freeCell = cell