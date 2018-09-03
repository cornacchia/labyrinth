import curses
from board import Board
from view import View

class Game:
  def __init__(self, players):
    self.players = players
    self.gameState = {'currentPlayer': 0, 'freeCellPositioning': True, 'moving': False}

  def start(self):
    self.gameBoard = Board(self.players)
    curses.wrapper(self.main)

  def main(self, stdscr):
    self.view = View(stdscr)
    self.view.setBoard(self.gameBoard)

    while (True):
      self.view.render(self.gameState, self.players)
      cmd = stdscr.getch()
      self.handleCmd(cmd)

  def handleCmd(self, cmd):
    if (self.gameState['freeCellPositioning']):
      if (cmd == ord('r')):
        self.gameBoard.freeCell.rotate(1)
      elif (cmd == curses.KEY_ENTER or cmd == 10 or cmd == 13):
        self.insertFreeCell()
      else:
        self.moveFreeCell(cmd)
    elif (self.gameState['moving']):
      if (cmd == curses.KEY_ENTER or cmd == 10 or cmd == 13):
        self.gameBoard.checkTreasures(self.gameState['currentPlayer'])
        self.gameState['currentPlayer'] = (self.gameState['currentPlayer'] + 1) % len(self.players)
        self.gameState['moving'] = False
        self.gameState['freeCellPositioning'] = True
      else:
        self.movePlayer(cmd)

  def movePlayer(self, cmd):
    if (cmd == curses.KEY_UP):
      self.gameBoard.movePlayer(self.gameState['currentPlayer'], 0)
    elif (cmd == curses.KEY_DOWN):
      self.gameBoard.movePlayer(self.gameState['currentPlayer'], 2)
    elif (cmd == curses.KEY_LEFT):
      self.gameBoard.movePlayer(self.gameState['currentPlayer'], 3)
    elif (cmd == curses.KEY_RIGHT):
      self.gameBoard.movePlayer(self.gameState['currentPlayer'], 1)

  def moveFreeCell(self, cmd):
    maxX = len(self.gameBoard.cells)
    maxY = len(self.gameBoard.cells[0])
    if (cmd == curses.KEY_UP and self.gameBoard.freeCell.freeX > -1 and self.gameBoard.freeCell.freeX < maxX):
      self.gameBoard.freeCell.freeX += -1
      if (self.gameBoard.freeCell.freeX == -1):
        self.adjustFreeCellY()
    elif (cmd == curses.KEY_DOWN and self.gameBoard.freeCell.freeX < maxX and self.gameBoard.freeCell.freeX > -1):
      self.gameBoard.freeCell.freeX += 1
      if (self.gameBoard.freeCell.freeX == maxX):
        self.adjustFreeCellY()
    elif (cmd == curses.KEY_LEFT and self.gameBoard.freeCell.freeY > -1 and self.gameBoard.freeCell.freeY < maxY):
      self.gameBoard.freeCell.freeY += -1
      if (self.gameBoard.freeCell.freeY == -1):
        self.adjustFreeCellX()
    elif (cmd == curses.KEY_RIGHT and self.gameBoard.freeCell.freeY < maxY and self.gameBoard.freeCell.freeY > -1):
      self.gameBoard.freeCell.freeY += 1
      if (self.gameBoard.freeCell.freeY == maxY):
        self.adjustFreeCellX()

  def adjustFreeCellY(self):
    maxY = len(self.gameBoard.cells[0])
    if (self.gameBoard.freeCell.freeY == -1):
      self.gameBoard.freeCell.freeY = 0
    elif (self.gameBoard.freeCell.freeY == maxY):
      self.gameBoard.freeCell.freeY = maxY - 1

  def adjustFreeCellX(self):
    maxX = len(self.gameBoard.cells)
    if (self.gameBoard.freeCell.freeX == -1):
      self.gameBoard.freeCell.freeX = 0
    elif (self.gameBoard.freeCell.freeX == maxX):
      self.gameBoard.freeCell.freeX = maxX - 1

  def insertFreeCell(self):
    # check if the move is permitted
    x = self.gameBoard.freeCell.freeX
    y = self.gameBoard.freeCell.freeY
    if ((x > 0 and (x % 2) != 0) or (y > 0 and (y % 2) != 0)):
      self.gameState['freeCellPositioning'] = False
      self.gameState['moving'] = True
      self.gameBoard.insertFreeCell()