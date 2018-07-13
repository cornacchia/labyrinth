import curses

charMap = [
  [False, False, 0, False, False],
  [3, '[', 'T', ']', 1],
  [False, False, 2, False, False]
]

class View:
  def __init__(self, stdscr):
    self.boardStartX = 0
    self.boardStartY = 0
    self.stdscr = stdscr
    self.boardBox = curses.newwin(80, 80, 0, 0)
    self.boardBox.immedok(True)
    self.boardBox.box()

  def setBoard(self, board):
    self.board = board

  def render(self):
    self.stdscr.clear()
    self.stdscr.refresh()

    for i in range(len(self.board.cells)):
      for j in range(len(self.board.cells[i])):
        cell = self.board.cells[i][j]
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
              if (cell.player):
                self.boardBox.addstr(y, x, '@')
              elif (cell.treasure):
                self.boardBox.addstr(y, x, str(cell.treasure))
              else:
                self.boardBox.addstr(y, x, ' ')
            else:
              if cell.exits[charMap[k][q]] > 0:
                if (k == 1):
                  self.boardBox.addstr(y, x, '-')
                else:
                  self.boardBox.addstr(y, x, '|')