from cell import Cell
import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for x in range(width)] for y in range(height)]
        self.bombs_arr = []

    def generate_board(self, bombs, x, y):
        bombs_arr = self.generate_bombs(bombs, x, y)

        for bomb in bombs_arr:
            bomb_x, bomb_y = bomb
            print(bomb_x, bomb_y)
            self.cells[bomb_y][bomb_x].is_mine = True

        for row in self.cells:
            for cell in row:
                if not cell.is_mine:
                    cell.set_neighbor_mines(self.count_bombs_around(cell))

        chk = ""
        for row in self.cells:
            for cell in row:
                chk += f'{cell.neighbor_mines} '
            print(chk)
            chk = ""

        pass

    def count_bombs_around(self, cell):
        count = 0
        for i in range(cell.y - 1, cell.y + 2):
            for j in range(cell.x - 1, cell.x + 2):
                if 0 <= i < self.height and 0 <= j < self.width and self.cells[i][j].is_mine:
                    count += 1
        return count

    def generate_bombs(self, bombs, cell_x, cell_y):
        print(bombs)
        bombs_arr = []
        for _ in range(bombs):
            while True:
                x, y = random.randint(0, bombs-1), random.randint(0, bombs-1)

                if self.is_not_in_proximity(x, y, cell_x, cell_y) and [x, y] not in bombs_arr:
                    bombs_arr.append([x, y])
                    break

        self.bombs_arr = bombs_arr
        return bombs_arr

    def get_bombs_arr(self):
        return self.bombs_arr

    def is_not_in_proximity(self, x, y, center_x, center_y):
        return abs(x - center_x) > 2 or abs(y - center_y) > 2


    def __repr__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.cells])