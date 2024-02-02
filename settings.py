#Game Settings
snake_speed = 150





#fps
fps = 60

#Color Settings
background_color = (160, 196, 100)
snake_color = (43, 51, 24)

#Grid Size Settings
cell_size = 30
number_of_cells = 25

#Do not change
if cell_size * number_of_cells > 1280:
    raise ValueError("The cell size * number of cells must equal 750.")


#Tuple is fetched from the cell size and number of cells above
screen_size = (cell_size*number_of_cells, cell_size*number_of_cells)

