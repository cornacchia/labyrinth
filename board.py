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

class Board:
  def __init__(self, players):
    # this is the cell out of the board
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

  # create empty cells list
  def createBlankCells(self):
    cells = [[] for i in range(7)]
    for cell in cells:
      for i in range(7):
        cell.append(None)
    return cells

  # set cells which positions are fixed for every game
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

  # set randomly scattered cells
  def setOtherCells(self):
    otherCells = []
    treasure = 12 # we have already positioned 12 treasures in fixed cells
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

  def shiftColumn(self, column, direction):
    # 1 -> down, -1 -> up
    lenX = len(self.cells[0])
    lenY = len(self.cells)
    newFreeCell = None

    if (direction > 0):
      newFreeCell = self.cells[lenX - 1][column]
      i = lenY - 1
      while (i > 0):
        self.cells[i][column] = self.cells[i - 1][column]
        i -= 1
    elif (direction < 0):
      newFreeCell = self.cells[0][column]
      i = 0
      while (i < lenY - 1):
        self.cells[i][column] = self.cells[i + 1][column]
        i += 1
    return newFreeCell

  def insertFreeCell(self):
    cell = self.freeCell
    lenX = len(self.cells[0])
    lenY = len(self.cells)
    x = cell.freeX
    y = cell.freeY
    cell.freeX = -1
    cell.freeY = 0
    if (y == -1):
      self.cells[x].insert(0, cell)
      self.freeCell = self.cells[x].pop(lenX)
    elif (y == lenX):
      self.cells[x].append(cell)
      self.freeCell = self.cells[x].pop(0)
    elif (x == -1):
      self.freeCell = self.shiftColumn(y, 1)
      self.cells[0][y] = cell
    elif (x == lenY):
      self.freeCell = self.shiftColumn(y, -1)
      self.cells[lenY - 1][y] = cell

    # check that the player is not out of the board
    if (self.freeCell.player is not None):
      if (y == -1):
        self.cells[x][0].player = self.freeCell.player
      elif (y == lenX):
        self.cells[x][lenX - 1].player = self.freeCell.player
      elif (x == -1):
        self.cells[0][y].player = self.freeCell.player
      elif (x == lenY):
        self.cells[lenY - 1][y].player = self.freeCell.player
      self.freeCell.player = None