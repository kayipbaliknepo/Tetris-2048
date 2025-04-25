import lib.stddraw as stddraw  # used for drawing the tiles to display them
from lib.color import Color  # used for coloring the tiles
import random

# A class for modeling numbered tiles as in 2048
class Tile:
   # Class variables shared among all Tile objects
   # ---------------------------------------------------------------------------
   # the value of the boundary thickness (for the boxes around the tiles)
   boundary_thickness = 0.004
   # font family and font size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # A constructor that creates a tile with 2 as the number on it
   def __init__(self):
        self.number = random.choice([2, 4])
        self.set_colors()

   def set_colors(self):
        if self.number == 2 or self.number == 4:
            self.background_color = Color(255, 200, 100)  # Hafif turuncu
            self.foreground_color = Color(255, 255, 255)  # Beyaz yazı
            self.box_color = Color(255, 230, 180)  # Açık kenar
        elif self.number == 8 or self.number == 16:
            self.background_color = Color(255, 160, 50)  # Daha koyu turuncu
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(255, 210, 160)
        else:
            self.background_color = Color(220, 70, 20)  # Kırmızımsı turuncu
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(255, 200, 180)


   # A method for drawing this tile at a given position with a given length
   def draw(self, position, length=1):  # length defaults to 1
      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(position.x, position.y, length / 2)
      # draw the bounding box around the tile as a square
      stddraw.setPenColor(self.box_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(position.x, position.y, length / 2)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.text(position.x, position.y, str(self.number))
