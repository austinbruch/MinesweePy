class Square(object):
   """Square class is used to represent a single tile within the game board"""

   states = ['Hidden', 'Flagged', 'Question', 'Revealed']

   def __init__(self, mine=False):
      super(Square, self).__init__()
      self.mine = mine
      self.state = Square.states[0]
      self.adj_mines = 0

   def __repr__(self):
      if self.mine:
         return "X"
      else:
         return str(self.adj_mines)

   def reveal(self):
      self.state = Square.states[3]

   def handle_right_click(self):
      if self.state == Square.states[0]:
         self.state = Square.states[1]

      if self.state == Square.states[1]:
         self.state = Square.states[2]

      if self.state == Square.states[2]:
         self.state = Square.states[0]


      