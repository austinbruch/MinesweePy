from Game import Game
from Board import Board

class MinesweePy(object):
   """docstring for MinesweePy"""
   def __init__(self, x_dim=9, y_dim=9, num_mines=10):
      super(MinesweePy, self).__init__()
      self.game = Game(x_dim, y_dim, num_mines)
      self.board = Board(x_dim, y_dim, self.game)
   
   # def map_game_to_board(self):

   
def main():
   minesweeper = MinesweePy(9, 9, 10)
   # minesweeper.game.print_status()
   minesweeper.board.parent.mainloop()

if __name__ == '__main__':
   main()      