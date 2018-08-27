import curses
from board import Board
from view import View

class Game:
  def __init__(self, players):
    self.players = players

  def start(self):
    self.gameBoard = Board(self.players)
    curses.wrapper(self.main)

  def main(self, stdscr):
    self.view = View(stdscr)
    self.view.setBoard(self.gameBoard)

    while (True):
      self.view.render()
      cmd = stdscr.getch()
      self.handleCmd(cmd)

  def handleCmd(self, cmd):
    if (cmd == ord('r')):
      self.gameBoard.freeCell.rotate(1)