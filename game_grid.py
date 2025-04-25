import lib.stddraw as stddraw  # used for displaying the game grid
from lib.color import Color  # used for coloring the game grid
from point import Point  # used for tile positions
import numpy as np  # fundamental Python module for scientific computing

# A class for modeling the game grid
class GameGrid:
   # A constructor for creating the game grid based on the given arguments
   def __init__(self, grid_h, grid_w):
      # set the dimensions of the game grid as the given arguments
      self.grid_height = grid_h
      self.grid_width = grid_w
      # create a tile matrix to store the tiles locked on the game grid
      self.tile_matrix = np.full((grid_h, grid_w), None)
      # create the tetromino that is currently being moved on the game grid
      self.current_tetromino = None
      # the game_over flag shows whether the game is over or not
      self.game_over = False
      # set the color used for the empty grid cells
      self.empty_cell_color = Color(245, 222, 179)
      # set the colors used for the grid lines and the grid boundaries
      self.line_color = Color(210, 180, 140)
      self.boundary_color = Color(210, 180, 140)
      # thickness values used for the grid lines and the grid boundaries
      self.line_thickness = 0.002
      self.box_thickness = 10 * self.line_thickness
      self.score = 0
      self.next_tetromino = None

   # A method for displaying the game grid
   # A method for displaying the game grid
   def display(self):
      # clear the background
      stddraw.clear(self.empty_cell_color)

      # draw the game grid
      self.draw_grid()
      # --- Skoru ekrana yaz ---
      stddraw.setPenColor(Color(255, 255, 255))  # Beyaz renk
      stddraw.setFontFamily("Arial")
      stddraw.setFontSize(20)
      stddraw.text(self.grid_width + 3, self.grid_height - 1, f"Score: {self.score}")

      # draw the current/active tetromino if it is not None
      if self.current_tetromino is not None:
         self.current_tetromino.draw()

      # draw the next tetromino on the right side if it is not None
      if self.next_tetromino is not None:
         print("Next tetromino var, çiziyorum!")
         n = len(self.next_tetromino.tile_matrix)
         for row in range(n):
               for col in range(n):
                  if self.next_tetromino is not None:
                     n = len(self.next_tetromino.tile_matrix)
                     for row in range(n):
                        for col in range(n):
                              if self.next_tetromino.tile_matrix[row][col] is not None:
                                 pos = Point()
                                 pos.x = self.grid_width + 1 + col + 0.5
                                 pos.y = self.grid_height - 6 + (n - 1 - row) + 0.5
                                 self.next_tetromino.tile_matrix[row][col].draw(pos)

         # write "NEXT" text above the box
         stddraw.setPenColor(Color(255, 0, 0))  # kırmızı renk
         stddraw.setFontFamily("Arial")
         stddraw.setFontSize(25)
         stddraw.text(self.grid_width + 3, self.grid_height - 1, "NEXT")

      # draw the box for the next tetromino
      stddraw.setPenColor(Color(255, 255, 255))  # beyaz renk kutu için
      stddraw.setPenRadius(0.002)  # kutunun kenar kalınlığı
      box_x = self.grid_width + 1
      box_y = self.grid_height - 6
      box_w = 4
      box_h = 4
      stddraw.rectangle(box_x, box_y, box_w, box_h)
      stddraw.setPenRadius()  # kalınlığı eski haline döndür
      # draw a box around the game grid
      self.draw_boundaries()
      if self.game_over:
         stddraw.setPenColor(Color(255, 0, 0))  # Kırmızı renk
         stddraw.setFontFamily("Arial")
         stddraw.setFontSize(40)
         stddraw.text(self.grid_width / 2, self.grid_height / 2, "GAME OVER")

      # draw the score
      stddraw.setPenColor(Color(255, 255, 255))  # White color
      stddraw.setFontFamily("Arial")
      stddraw.setFontSize(20)
      stddraw.text(self.grid_width, self.grid_height - 1, f"Score: {self.score}")

      # show the resulting drawing with a pause duration = 250 ms
      stddraw.show(250)
      # A method for drawing the cells and the lines of the game grid
   def draw_grid(self):
      # for each cell of the game grid
      for row in range(self.grid_height):
         for col in range(self.grid_width):
            # if the current grid cell is occupied by a tile
            if self.tile_matrix[row][col] is not None:
               # draw this tile
               self.tile_matrix[row][col].draw(Point(col, row))
            else:
                # boş hücreyi açık renkle doldur
                stddraw.setPenColor(Color(245, 245, 220))  # very light orange / krem rengi
                stddraw.filledSquare(col, row, 0.5)
      # draw the inner lines of the game grid
      stddraw.setPenColor(self.line_color)
      stddraw.setPenRadius(self.line_thickness)
      # x and y ranges for the game grid
      start_x, end_x = -0.5, self.grid_width - 0.5
      start_y, end_y = -0.5, self.grid_height - 0.5
      for x in np.arange(start_x + 1, end_x, 1):  # vertical inner lines
         stddraw.line(x, start_y, x, end_y)
      for y in np.arange(start_y + 1, end_y, 1):  # horizontal inner lines
         stddraw.line(start_x, y, end_x, y)
      stddraw.setPenRadius()  # reset the pen radius to its default value

   # A method for drawing the boundaries around the game grid
   def draw_boundaries(self):
      # draw a bounding box around the game grid as a rectangle
      stddraw.setPenColor(self.boundary_color)  # using boundary_color
      # set the pen radius as box_thickness (half of this thickness is visible
      # for the bounding box as its lines lie on the boundaries of the canvas)
      stddraw.setPenRadius(self.box_thickness)
      # the coordinates of the bottom left corner of the game grid
      pos_x, pos_y = -0.5, -0.5
      stddraw.rectangle(pos_x, pos_y, self.grid_width, self.grid_height)
      stddraw.setPenRadius()  # reset the pen radius to its default value

   # A method used checking whether the grid cell with the given row and column
   # indexes is occupied by a tile or not (i.e., empty)
   def is_occupied(self, row, col):
      # considering the newly entered tetrominoes to the game grid that may
      # have tiles with position.y >= grid_height
      if not self.is_inside(row, col):
         return False  # the cell is not occupied as it is outside the grid
      # the cell is occupied by a tile if it is not None
      return self.tile_matrix[row][col] is not None

   # A method for checking whether the cell with the given row and col indexes
   # is inside the game grid or not
   def is_inside(self, row, col):
      if row < 0 or row >= self.grid_height:
         return False
      if col < 0 or col >= self.grid_width:
         return False
      return True

   # A method that locks the tiles of a landed tetromino on the grid checking
   # if the game is over due to having any tile above the topmost grid row.
   # (This method returns True when the game is over and False otherwise.)
   def update_grid(self, tiles_to_lock, blc_position):
    self.current_tetromino = None
    n_rows, n_cols = len(tiles_to_lock), len(tiles_to_lock[0])

    for col in range(n_cols):
        for row in range(n_rows):
            if tiles_to_lock[row][col] is not None:
                pos = Point()
                pos.x = blc_position.x + col
                pos.y = blc_position.y + (n_rows - 1) - row

                print(f"Tile going to: ({pos.x}, {pos.y})")

                if self.is_inside(pos.y, pos.x):
                    self.tile_matrix[pos.y][pos.x] = tiles_to_lock[row][col]
                else:
                    # Eğer pozisyon grid'in üstünü aşarsa oyun biter
                    if pos.y >= self.grid_height:
                        print("GAME OVER because of tile at:", pos.x, pos.y)
                        self.game_over = True
                        return True  # Dön ve ana döngüyü bitir
    return self.game_over


   # Skoru güncelle
   def update_score(self, points):
      self.score += points

   # Merge işlemleri ve satır temizleme
   def merge_tiles(self):
    merged = False
    # Her sütunda, alttaki hücreden başlayarak zincirleme birleşmeyi uygula
    for col in range(self.grid_width):
        # Boş olmayan taşları al, alttan üste doğru
        values = [self.tile_matrix[row][col] for row in range(self.grid_height)
                  if self.tile_matrix[row][col] is not None]
        # Zincir birleşme: ardışık eşit değer kalmayana dek tekrar et
        while True:
            merged_in_pass = False
            for i in range(len(values) - 1):
                if values[i].number == values[i + 1].number:
                    # Birleştir ve üstteki taşı sil
                    values[i].number *= 2
                    del values[i + 1]
                    merged = True
                    merged_in_pass = True
                    break
            if not merged_in_pass:
                break
        # Yeniden matrise yaz: değerler en altta başlar, üstüne None ekle
        for row in range(self.grid_height):
            if row < len(values):
                self.tile_matrix[row][col] = values[row]
            else:
                self.tile_matrix[row][col] = None
    self.clear_full_lines()
    return merged
   # Tam dolu satırları temizler
   def clear_full_lines(self):
    cleared_any = False
    rows_to_clear = []

    for row in range(self.grid_height):
        if all(self.tile_matrix[row][col] is not None for col in range(self.grid_width)):
            rows_to_clear.append(row)

    if rows_to_clear:
        cleared_any = True
        for row in rows_to_clear:
            # Satırı boşalt
            self.tile_matrix[row] = [None for _ in range(self.grid_width)]

        # Temizlenen satırların üstündeki satırları aşağı kaydır
        for row in reversed(range(self.grid_height)):
            if all(self.tile_matrix[row][col] is None for col in range(self.grid_width)):
                # Yukarıdaki dolu satırı bulup kopyala
                for r in range(row, self.grid_height - 1):
                    self.tile_matrix[r] = self.tile_matrix[r + 1]
                # En üst satırı boş yap
                self.tile_matrix[self.grid_height - 1] = [None for _ in range(self.grid_width)]

    return cleared_any