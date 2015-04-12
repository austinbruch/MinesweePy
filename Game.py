from Square import Square
import random

class Game(object):
   """docstring for Game"""
   def __init__(self, x_dim, y_dim, num_mines):
      super(Game, self).__init__()
      self.x = x_dim
      self.y = y_dim
      self.mines = num_mines
      # TODO: Validation
      self.populate()
      

   def populate(self):
      self.grid = [[Square() for i in range(self.x)] for i in range(self.y)]
      
      # plot the mines
      count = 0
      while count != self.mines:
         mine_x = random.randint(0, self.x-1)
         mine_y = random.randint(0, self.y-1)
         if self.grid[mine_x][mine_y].mine == False:  # If this square isn't already a mine, make it one
            self.grid[mine_x][mine_y].mine = True
            count = count + 1

      # update adjacent mine counts
      for i in range(0,self.x):
         for j in range(0,self.y):
            if self.grid[i][j].mine == False: # Only calculate number of adjacent mines for mineless squares
               count = 0
               # left
               if self.is_mine(i-1, j):
                  count = count + 1
               # up-left
               if self.is_mine(i-1, j-1):
                  count = count + 1
               # up
               if self.is_mine(i, j-1):
                  count = count + 1
               # up-right
               if self.is_mine(i+1, j-1):
                  count = count + 1
               # right
               if self.is_mine(i+1, j):
                  count = count + 1
               # down-right
               if self.is_mine(i+1, j+1):
                  count = count + 1
               # down
               if self.is_mine(i, j+1):
                  count = count + 1
               # down-left
               if self.is_mine(i-1, j+1):
                  count = count + 1

               self.grid[i][j].adj_mines = count
               

   def is_mine(self, x, y):
      if x in range(0, self.x) and y in range(0, self.y):
         return self.grid[x][y].mine
      else:
         return False

   def print_status(self):
      for square in self.grid:
         print(square)