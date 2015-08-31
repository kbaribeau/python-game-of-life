class Gol:
    def will_be_alive_in_next_generation(self, is_cell_alive, num_alive_neighbours):
        if is_cell_alive:
            return num_alive_neighbours == 2 or num_alive_neighbours == 3
        else:
            return num_alive_neighbours == 3

    def count_neighbours(self, grid, coords):
        def normalize_coords(x, y):
            maxx = len(grid[0])
            maxy= len(grid)
            if x == maxx:
                x = 0
            if y == maxy:
                y = 0
            return (x, y)

        x, y = coords
        result = 0
        for neighbourx in range(x-1, x+2):
            for neighboury in range(y-1, y+2):
                if (x, y) != (neighbourx, neighboury):
                    neighbourx, neighboury = normalize_coords(neighbourx, neighboury)
                    result += grid[neighbourx][neighboury]

        return result


