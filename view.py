import curses

# this list's values are needed to render the cell
charMap = [
  [False, False, 0, False, False],
  [3, '[', 'T', ']', 1],
  [False, False, 2, False, False]
]

class View:
  def __init__(self, stdscr):
    self.boardStartX = 6
    self.boardStartY = 6
    self.stdscr = stdscr
    self.boardBox = curses.newwin(80, 80, 0, 0)
    self.boardBox.immedok(True)
    self.boardBox.box()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

  def setBoard(self, board):
    self.board = board

  def render(self, state):
    self.stdscr.clear()
    self.stdscr.refresh()

    # draw game board
    for i in range(len(self.board.cells)):
      for j in range(len(self.board.cells[i])):
        cell = self.board.cells[i][j]
        self.drawCell(cell, i, j)

    # draw free cell
    self.drawFreeCell(self.board.freeCell)

  def drawCell(self, cell, i, j):
    for k in range(len(charMap)):
      for q in range(len(charMap[k])):
        x = self.boardStartX + (len(charMap[0]) * j) + q
        y = self.boardStartY + (len(charMap) * i) + k

        if charMap[k][q] is False:
          self.boardBox.addstr(y, x, ' ')
        elif charMap[k][q] == '[':
          self.boardBox.addstr(y, x, '[')
        elif charMap[k][q] == ']':
          self.boardBox.addstr(y, x, ']')
        elif charMap[k][q] == 'T':
          if (cell.players[0]):
            self.boardBox.addstr(y, x, '@', curses.color_pair(1))
          elif (cell.players[1]):
            self.boardBox.addstr(y, x, '@', curses.color_pair(2))
          elif (cell.players[2]):
            self.boardBox.addstr(y, x, '@', curses.color_pair(3))
          elif (cell.players[3]):
            self.boardBox.addstr(y, x, '@', curses.color_pair(4))
          elif (cell.treasure):
            self.boardBox.addstr(y, x, str(cell.treasure))
          else:
            self.boardBox.addstr(y, x, ' ')
        else:
          if cell.exits[charMap[k][q]] > 0:
            # horizontal exits
            if (k == 1):
              self.boardBox.addstr(y, x, '-')
            # vertical exits
            else:
              self.boardBox.addstr(y, x, '|')

  def drawFreeCell(self, freeCell):
    self.drawCell(freeCell, freeCell.freeX, freeCell.freeY)