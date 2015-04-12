from Tkinter import Tk, BOTH, SUNKEN, RAISED, Frame, Button, Label

class Board(Frame):

   def __init__(self, x_dim, y_dim, game, parent=Tk()):
      Frame.__init__(self, parent)

      self.game = game
      self.parent = parent
      self.x = x_dim
      self.y = y_dim

      self.initUI()

   def initUI(self):

      self.parent.title("MinesweePy")

      for i in range(0, self.x):
         self.columnconfigure(i, pad=0)
         
      for i in range(0, self.y):
         self.rowconfigure(i, pad=0)

      for i in range(0, self.x):
         for j in range(0, self.y):
            button = Button(self, text=" ", borderwidth=0, relief=RAISED)
            button.grid(row=i, column=j)
            button.bind('<Button-1>', on_single_left_click)
            button.bind('<Button-2>', on_right_click)
            button.square = self.game.grid[i][j]

      self.pack()

def on_single_left_click(event):
      print("Single Clicked")
      event.widget.config(relief=SUNKEN)
      event.widget.config(text=event.widget.square.__repr__())

def on_double_left_click(event):
   print("Double Clicked")

def on_right_click(event):
   print("Right Clicked")
