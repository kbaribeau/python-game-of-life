# Implementation of Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


class GameOfLife(object):

    def will_cell_be_alive_in_next_generation(self, is_cell_alive, num_alive_neighbours):
        """
        Determine whether a given cell state will be alive given its number of alive neighbours
        """
        if is_cell_alive:
            return num_alive_neighbours == 2 or num_alive_neighbours == 3
        else:
            return num_alive_neighbours == 3

    def count_alive_neighbours(self, grid, coordinates):
        """
        Given a grid and a set of coordinates, determine the number of live neighbors for the given cell
        """

        def normalize_coordinates(x, y):
            """
            Account for wrapping of the grid.  E.g., the neighbour to a cell on the far right of the grid is the cell on
            the far left of the grid.  Similarly, the neighbour to a cell on the far bottom of the grid is the cell on
            the far top of the grid.
            """
            max_x = len(grid[0])
            max_y = len(grid)

            # Account for right and bottom edge-wrapping
            if x == max_x:
                x = 0
            if y == max_y:
                y = 0

            # Account for left and top edge-wrapping (e.g., when a coordinate is already a negative number)
            if x == -1:
                x = max_x - 1
            if y == -1:
                y = max_y - 1

            return x, y

        x, y = coordinates
        alive_neighbours = 0
        for neighbour_x in range(x-1, x+2):
            for neighbour_y in range(y-1, y+2):
                if (x, y) != (neighbour_x, neighbour_y):
                    norm_neighbour_x, norm_neighbour_y = normalize_coordinates(neighbour_x, neighbour_y)
                    alive_neighbours += grid[norm_neighbour_y][norm_neighbour_x]


        return alive_neighbours

    def determine_next_grid(self, input_grid):
        """
        Given any input grid, determine the next state of the grid.
        """
        max_x = len(input_grid[0])
        max_y = len(input_grid)
        output_grid = [[0 for output_x in range(max_x)] for output_y in range(max_y)]
        for x in range(0, max_x):
            for y in range(0, max_y):
                num_alive_neighbours = self.count_alive_neighbours(input_grid, (x, y))
                is_alive = self.will_cell_be_alive_in_next_generation(input_grid[y][x], num_alive_neighbours)
                if is_alive:
                    output_grid[y][x] = 1
        return output_grid

if __name__=='__main__':
  import time
  gol = GameOfLife()
  # http://www.conwaylife.com/wiki/R-pentomino
  grid = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,0,0,0,0],
          [0,0,0,1,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]
  while True:
    for line in grid:
      print line
    print ''
    grid = gol.determine_next_grid(grid)
    time.sleep(1)
